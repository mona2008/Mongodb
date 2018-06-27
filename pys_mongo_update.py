from pymongo import MongoClient
import pprint
client=MongoClient()
db=client.test_database
def main():
    grocery=db.groce.find_one({"item":"pen","qty":20})
    grocery["cost"]=200
    db.groce.save(grocery)
if __name__=="__main__":
    main()
