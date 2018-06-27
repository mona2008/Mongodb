from pymongo import MongoClient
client=MongoClient()  #the above 2 lines are used for making onnection to mongodb
db=client.datab2  #creating a database of name datab1
collection = db['orgname'] 

#Creating a collection
#since the document does not specify an _id field, MongoDB adds the _id field with an ObjectId value to the new document

db.orgname.insert({"id": "1", "name": "Monika", "org":"Infosys"})
db.orgname.insert({"id": "2", "name":"Lalit", "org":"IBM"})
db.orgname.insert({"id": "3", "name":"Purva", "org":"TCS"})
db.orgname.insert({"id": "4", "name":"Ganesh", "org":"Google"})

#insertOne()inserts one document in the array
#db.orgname.insertOne({"id":5,"name":"Sahil","org":"facebook"})

#insertMany() inserts each document in the array into the collection.
#db.orgname.insertMany([{"id":"5","name":"Sahil","org":"facebook"},{"id": "6","name":"Ranbir Kapoor","org":"bollywood"},{"id":"7","name":"Jackky","org":"Adidas"}])

#Read operation
print("show database after creating\n",list(db.orgname.find()))

#if we want to find information about particular data then use this syntax.
#print("show database after creating\n",list(db.orgname.find({"org":"Google","name":Purva"})))

#Update
db.orgname.update({"name":"Lalit"},{"$set":{"org":"Google"}})
print("show database after updation\n",list(db.orgname.find()))

#updateOne update the first document where id equals 3.
#db.orgname.updateOne({id=3},{$set:{"name":"Kamal"}})

#updateMany method on the orgname collection update all documents where "org" is Google.
#db.orgname.updateMany({"org":"Google"},{$set:{"name":"Kamalpreet"}})
#$set is used to modify field values

#db.collection.replaceOne() method on the orgname collection to replace the first document matches the filter name equals "Lalit"

#Deleting the collection
#db.orgname.drop()
#print("show database after deletion\n",list(db.orgname.find()))
