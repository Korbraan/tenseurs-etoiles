import query
import fileManager
from ownParser import parseFile
from query import *
import requests
import time
from fileManager import save, load, FILE
import csv
import os
import json

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

with open("data"+os.sep+"training_set_91_91.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"): #You can also use delimiter="\t" rather than giving a dialect.
        print("params : ", line[0],line[1])
       # res = requestSPARQLParam(line[0],line[1],queryDrugBankParam)
        #print(res)

with open("data.file", mode='w', encoding='utf-8') as f:
    json.dump([], f)

with open("data.file", mode='r+', encoding='utf-8') as feedsjson:
    feeds = json.load(feedsjson)
    print(feeds)
    entry = {'name': 'mon chibre', 'url': 'veineux'}
    feeds.append(entry)
    print(feeds)
    entry = {'name': 'mabite', 'url': 'poilueducul'}
    feeds.append(entry)
    json.dump(feeds, feedsjson,indent=2)