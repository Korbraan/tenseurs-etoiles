query = """
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

CONSTRUCT {}
WHERE {
    pharmgkb:%(gene)s pharmgkbv:x-drugbank ?drug2.
    pharmgkb:%(gene)s pharmgkbv:x-umls ?cui.
    pharmgkb:%(gene)s pharmgkbv:x-pubchemcompound ?compound.
    ?drug3 siderv:pubchem-flat-compound-id ?compound.
    ?drug_target dbv:drug ?drug2.
    ?drug_target dbv:action ?action.
    ?drug2 dbv:x-pubchemcompound ?compound.
    ?drug2 dbv:x-atc ?atc.
    ?drug_target dbv:target ?target.
    ?target dbv:x-uniprot ?prot.
    pharmgkb:%(drug)s pharmgkbv:x-uniprot ?prot.
    pharmgkb:%(drug)s pharmgkbv:x-ncbigene ?gene.
    ?gene2 clinvarv:x-gene ?gene.
    ?gene2 clinvarv:x-sequence_ontology ?so.
    ?rcv clinvarv:Variant_Gene ?gene2.
    ?rcv clinvarv:Variant_Phenotype ?x.
    ?x clinvarv:x-medgen ?disease2.
    ?gene bio2rdfv:x-identifiers.org ?gene3.
    ?var sio:SIO_000628 ?gene3.
    ?var sio:SIO_000628 ?disease.
    ?gene3 sio:SIO_000062 ?react.
    ?disease sio:SIO_000095 ?mesh.
    ?disease sio:SIO_000008 ?semantic_type.
    ?disease skos:exactMatch ?disease2.
    ?drug3 siderv:side-effect ?disease3.
    ?disease skos:exactMatch ?disease3.
    ?disease4 mapping:medispan_to_sider ?disease3.
    ?disease2 mapping:clinvar_to_sider ?disease3.
    ?disease2 mapping:clinvar_to_medispan ?disease4.
}
"""
