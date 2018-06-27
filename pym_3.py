from pymongo import MongoClient
import pprint
client=MongoClient()
db=client.examples #examples is the database
def find():
    query={"surname":"singh","name":"monika"}
    projection={"year":0,"work":1}
    sets_table=db.sets_table.find(query,projection)
    for a in sets_table:
        pprint.pprint(a)

if __name__=="__main__":
    find()
