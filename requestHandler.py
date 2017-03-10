import query
import fileManager
from ownParser import parseFile
from query import query
import requests
import time
from fileManager import save, load, FILE

USER = 'student'
PASS = '5hoPpeR4'
HEADER = 'application/sparql-results+json'
ADDRESS = 'https://pgxlod.loria.fr/bigdata/namespace/kb/sparql'

def requestSPARQL(gene, drug):
    print ("Request for (%s, %s)" % (gene, drug)),
    res = requests.post(
        ADDRESS,
        auth=(USER, PASS),
        headers={'Accept': HEADER},
        data={'query': query % {'gene': gene, 'drug': drug}},
        verify=False
    )
    if res.status_code == 200:
        print ("[OK]"),
    else:
        print ("[FAIL]"),
    return res.content


res = requestSPARQL("PA7360","PA131301952")
print (res)

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

save(data, FILE)
