from pymongo import MongoClient
import pprint
client=MongoClient()
sets={"name":"monika","surname":"singh","id":2314026,"year":[2012,2017],"layout":["good","bad"],"designer":{"first":"tata","last":"motor"},"work":"student"}
db=client.examples #examples is the database
db.sets_table.insert(sets)#sets_table is the collection(table)
for a in db.sets_table.find():
    pprint.pprint(a)
'''  
def find():
    sets_table=db.sets_table.find({"surname":"singh"})
    for a in sets_table:
        pprint.pprint(a)

if __name__=="__main__":
    find()
'''
