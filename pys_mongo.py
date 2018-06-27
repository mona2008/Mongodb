from pymongo import Connection
if __name__=="__main__":
    con=Connection()
    #client=MongoClient()
    db=con.test_database
    people=db.people
    people.insert({'name':'monika','surname':'singh'})
    people.insert({'name':'lalit','surname':'sharma','id':1001})
    people.insert({'name':'purva','surname':'jain'})
    pree=people.find()
    print('insert and find test')
    for person in pree:
        print(person)
