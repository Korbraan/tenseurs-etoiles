queryDrugBank = """
PREFIX atc: <http://bio2rdf.org/atc:>
PREFIX bio2rdfv: <http://bio2rdf.org/bio2rdf_vocabulary:>
PREFIX clinvar: <http://bio2rdf.org/clinvar:>
PREFIX clinvarv: <http://bio2rdf.org/clinvar_vocabulary:>
PREFIX dbv: <http://bio2rdf.org/drugbank_vocabulary:>
PREFIX disgenet: <http://rdf.disgenet.org/resource/gda/>
PREFIX drugbank: <http://bio2rdf.org/drugbank:>
PREFIX mapping: <http://biodb.jp/mappings/>
PREFIX medispan: <http://orpailleur.fr/medispan/>
PREFIX ncbigene: <http://bio2rdf.org/ncbigene:>
PREFIX pharmgkb: <http://bio2rdf.org/pharmgkb:>
PREFIX pharmgkbv: <http://bio2rdf.org/pharmgkb_vocabulary:>
PREFIX pubchemcompound: <http://bio2rdf.org/pubchem.compound:>
PREFIX sider: <http://bio2rdf.org/sider:>
PREFIX siderv: <http://bio2rdf.org/sider_vocabulary:>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX so: <http://bio2rdf.org/sequence_ontology:>
PREFIX umls: <http://bio2rdf.org/umls:>
PREFIX uniprot: <http://bio2rdf.org/uniprot:>

SELECT DISTINCT ?relation ?gene ?action ?drug
WHERE {
  ?drug pharmgkbv:x-drugbank ?drugbank.
  ?relation dbv:drug ?drugbank.
  ?gene pharmgkbv:x-uniprot ?uniprot.
  ?drugbankGene dbv:x-uniprot ?uniprot.
  {?relation dbv:target ?drugbankGene}
  UNION {?relation dbv:carrier ?drugbankGene}
  UNION {?relation dbv:enzyme ?drugbankGene}
  UNION {?relation dbv:transporter ?drugbankGene}
  ?relation dbv:action ?action.
}
"""

queryDrugBankParam = """
PREFIX atc: <http://bio2rdf.org/atc:>
PREFIX bio2rdfv: <http://bio2rdf.org/bio2rdf_vocabulary:>
PREFIX clinvar: <http://bio2rdf.org/clinvar:>
PREFIX clinvarv: <http://bio2rdf.org/clinvar_vocabulary:>
PREFIX dbv: <http://bio2rdf.org/drugbank_vocabulary:>
PREFIX disgenet: <http://rdf.disgenet.org/resource/gda/>
PREFIX drugbank: <http://bio2rdf.org/drugbank:>
PREFIX mapping: <http://biodb.jp/mappings/>
PREFIX medispan: <http://orpailleur.fr/medispan/>
PREFIX ncbigene: <http://bio2rdf.org/ncbigene:>
PREFIX pharmgkb: <http://bio2rdf.org/pharmgkb:>
PREFIX pharmgkbv: <http://bio2rdf.org/pharmgkb_vocabulary:>
PREFIX pubchemcompound: <http://bio2rdf.org/pubchem.compound:>
PREFIX sider: <http://bio2rdf.org/sider:>
PREFIX siderv: <http://bio2rdf.org/sider_vocabulary:>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX so: <http://bio2rdf.org/sequence_ontology:>
PREFIX umls: <http://bio2rdf.org/umls:>
PREFIX uniprot: <http://bio2rdf.org/uniprot:>

SELECT (COUNT (?action) AS ?numberOfaction)
WHERE {
  pharmgkb:%(drug)s pharmgkbv:x-drugbank ?drugbank.
  ?relation dbv:drug ?drugbank.
  pharmgkb:%(gene)s pharmgkbv:x-uniprot ?uniprot.
  ?drugbankGene dbv:x-uniprot ?uniprot.
  {?relation dbv:target ?drugbankGene}
  UNION {?relation dbv:carrier ?drugbankGene}
  UNION {?relation dbv:enzyme ?drugbankGene}
  UNION {?relation dbv:transporter ?drugbankGene}
  ?relation dbv:action ?action.
}
"""

queryDiseaseParam="""
SELECT COUNT(DISTINCT ?disgeneDisease) AS ?numberOfDiseases
WHERE {
  %(gene)s pharmgkbv:x-ncbigene ?ncbigene.
  {
    ?ncbigene bio2rdfv:x-identifiers.org ?disgene.
    ?disgeneVar sio:SIO_000628 ?disgene.
    ?disgeneVar sio:SIO_000628 ?disgeneDisease.
    ?disgeneDisease skos:exactMatch ?siderDisease.
    %(drug)s pharmgkbv:x-pubchemcompound ?pubchem.
    ?siderdrug siderv:pubchem-flat-compound-id ?pubchem.
    {?siderdrug siderv:indication ?siderDisease}
    UNION {?siderdrug siderv:side_effect ?siderDisease}
  }

  UNION{
    ?ncbigene bio2rdfv:x-identifiers.org ?disgene.
    ?disgeneVar sio:SIO_000628 ?disgene.
    ?disgeneVar sio:SIO_000628 ?disgeneDisease.
    ?disgeneDisease skos:exactMatch ?medispanDisease.
    %(drug)s pharmgkbv:umls ?umls.
    ?medispanDrug mapping:medispan_to_umls ?umls.
    {?medispanDrug medispan:indication ?medispanDisease}
    UNION {?medispanDrug medispan:side_effect ?medispanDisease}
  }

  UNION{
    ?clinvarGene clinvarv:x-gene ?ncbigene.
    ?clinvarVar clinvarv:Variant_Gene ?clinvarGene.
    {?clinvarVar clinvarv:Variant_Phenotype ?clinvarDisease}
    UNION {?clinvarVar clinvar:x-medgen ?clinvarDisease}
    ?clinvarDisease mapping:clinvar_to_sider ?siderDisease.
    ?disgeneDisease skos:exactMatch ?clinvarDisease.
    %(drug)s pharmgkbv:x-pubchemcompound ?pubchem.
    ?siderdrug siderv:pubchem-flat-compound-id ?pubchem.
    {?siderdrug siderv:indication ?siderDisease}
    UNION {?siderdrug siderv:side_effect ?siderDisease}
  }

  UNION{
    ?clinvarGene clinvarv:x-gene ?ncbigene.
    ?clinvarVar clinvarv:Variant_Gene ?clinvarGene.
    {?clinvarVar clinvarv:Variant_Phenotype ?clinvarDisease}
    UNION {?clinvarVar clinvar:x-medgen ?clinvarDisease}
    ?clinvarDisease mapping:clinvar_to_medispan ?medispanDisease.
    ?disgeneDisease skos:exactMatch ?clinvarDisease.
    %(drug)s pharmgkbv:umls ?umls.
    ?medispanDrug mapping:medispan_to_umls ?umls.
    {?medispanDrug medispan:indication ?medispanDisease}
    UNION {?medispanDrug medispan:side_effect ?medispanDisease}
  }

}"""

queryBasic = """
PREFIX atc: <http://bio2rdf.org/atc:>
PREFIX bio2rdfv: <http://bio2rdf.org/bio2rdf_vocabulary:>
PREFIX clinvar: <http://bio2rdf.org/clinvar:>
PREFIX clinvarv: <http://bio2rdf.org/clinvar_vocabulary:>
PREFIX dbv: <http://bio2rdf.org/drugbank_vocabulary:>
PREFIX disgenet: <http://rdf.disgenet.org/resource/gda/>
PREFIX drugbank: <http://bio2rdf.org/drugbank:>
PREFIX mapping: <http://biodb.jp/mappings/>
PREFIX medispan: <http://orpailleur.fr/medispan/>
PREFIX ncbigene: <http://bio2rdf.org/ncbigene:>
PREFIX pharmgkb: <http://bio2rdf.org/pharmgkb:>
PREFIX pharmgkbv: <http://bio2rdf.org/pharmgkb_vocabulary:>
PREFIX pubchemcompound: <http://bio2rdf.org/pubchem.compound:>
PREFIX sider: <http://bio2rdf.org/sider:>
PREFIX siderv: <http://bio2rdf.org/sider_vocabulary:>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX so: <http://bio2rdf.org/sequence_ontology:>
PREFIX umls: <http://bio2rdf.org/umls:>
PREFIX uniprot: <http://bio2rdf.org/uniprot:>

SELECT DISTINCT ?relation ?action
WHERE {
  pharmgkb:PA449053 pharmgkbv:x-drugbank ?drugbank.
  ?relation dbv:drug ?drugbank.
  pharmgkb:PA107 pharmgkbv:x-uniprot ?uniprot.
  ?drugbankGene dbv:x-uniprot ?uniprot.
  {?relation dbv:target ?drugbankGene}
  UNION {?relation dbv:carrier ?drugbankGene}
  UNION {?relation dbv:enzyme ?drugbankGene}
  UNION {?relation dbv:transporter ?drugbankGene}
  ?relation dbv:action ?action.
}
"""