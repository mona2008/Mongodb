from pymongo import MongoClient
client=MongoClient()  #the above 2 lines are used for making onnection to mongodb
db=client.datab1  #creating a database of name datab1
collection = db['language'] 

#Creating a collection
#since the document does not specify an _id field, MongoDB adds the _id field with an ObjectId value to the new document

db.language.insert({"id": "1", "name": "Monika", "org":"Infosys"})
db.language.insert({"id": "2", "name":"Lalit", "org":"IBM"})
db.language.insert({"id": "3", "name":"Purva", "org":"TCS"})
db.language.insert({"id": "4", "name":"Ganesh", "org":"Google"})

#insertOne()inserts one document in the array
#db.language.insertOne({"id":5,"name":"Sahil","org":"facebook"})

#insertMany() inserts each document in the array into the collection.
#db.company.insertMany([{"id":"5","name":"Sahil","org":"facebook"},{"id": "6","name":"Ranbir Kapoor","org":"bollywood"},{"id":"7","name":"Jackky","org":"Adidas"}])

#Read operation
print("show database after creating\n",list(db.language.find()))

#if we want to find information about particular data then use this syntax.
#print("show database after creating\n",list(db.language.find({"org":"Google","name":Purva"})))

#Update
db.language.update({"name":"Lalit"},{"$set":{"org":"Google"}})
print("show database after updation\n",list(db.language.find()))

#updateOne update the first document where id equals 3.
#db.language.updateOne({id=3},{$set:{"name":"Kamal"}})

#updateMany method on the language collection update all documents where "org" is Google.
#db.inventory.updateMany({"org":"Google"},{$set:{"name":"Kamalpreet"}})
#$set is used to modify field values

#db.collection.replaceOne() method on the langauge collection to replace the first document matches the filter name equals "Lalit"

#Deleting the collection
#db.language.drop()
#print("show database after deletion\n",list(db.language.find()))
