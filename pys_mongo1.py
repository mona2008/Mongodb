from pymongo import MongoClient
import pprint
client=MongoClient()
tes={"name":"monika","clas":"3","surname":"singh"}
db=client.examples
db.autos.insert(tes)
for a in db.autos.find():
    pprint.pprint(a)
