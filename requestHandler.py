import query
import fileManager
from ownParser import parseFile
from query import *
import requests
import time
from fileManager import save, load, FILE
import csv
import os


USER = 'student'
PASS = '5hoPpeR4'
HEADER = 'application/sparql-results+json'
ADDRESS = 'https://pgxlod.loria.fr/bigdata/namespace/kb/sparql'

#A utiliser pour itérer sur chaque bidule couple
def requestSPARQLParam(gene, drug, queryChoice):
    print ("Request for (%s, %s)" % (gene, drug)),
    res = requests.post(
        ADDRESS,
        auth=(USER, PASS),
        headers={'Accept': HEADER},
        data={'query': queryChoice % {'gene': gene, 'drug': drug}},
        verify=False
    )
    if res.status_code == 200:
        print ("[OK]"),
    else:
        print ("[FAIL]"),
    return res.content
#Sans couple, balek
def requestSPARQL(queryChoice):
    print ("Request")
    res = requests.post(
        ADDRESS,
        auth=(USER, PASS),
        headers={'Accept': HEADER},
        data={'query': queryChoice},
        verify=False
    )
    if res.status_code == 200:
        print ("[OK]"),
    else:
        print ("[FAIL]"),
    return res.content


with open("data"+os.sep+"training_set_91_91.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"): #You can also use delimiter="\t" rather than giving a dialect.
        print("params : ", line[0],line[1])
        res = requestSPARQLParam(line[0],line[1],queryDrugBankParam)

#res1 = requestSPARQL(queryBasic)
#res = requestSPARQLParam("PA134879223","PA162372840",queryDrugBankParam)
save(res,FILE)
#print(res['body'])



#Ici il faut boucler sur les jeux d'entrainement pour récupérer quelquechose d'utile. Beaucoup de requêtes à lancer...
values = parseFile('./data/training_set_91_182.tsv')

data = []

l = len(values)
i = 1


#for value in values:
#    print ("[%d/%d]\t" % (i, l)),
#    res = requestSPARQL(gene=value[0], drug=value[1])
#    print (res)
#    i += 1
#    data.append({'gene': value[0], 'drug': value[1], 'asso': value[2], 'json': res})
#    print ("\n"),


