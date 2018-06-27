from pymongo import MongoClient
import pprint
client=MongoClient()
db=client.examples #examples is the database
#db.sets_table.insert(sets)#sets_table is the collection(table)
def find():
    sets_table=db.sets_table.find({"surname":"singh","name":"monika"}).pretty()
    for a in sets_table:
        pprint.pprint(a)

if __name__=="__main__":
    find()
