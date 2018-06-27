from pymongo import MongoClient
import pprint
client=MongoClient()
db=client.MyDB1
def insert():
    try:
        employeeId = raw_input('Enter Employee id :')
        employeeName = raw_input('Enter Name :')
        employeeAge = raw_input('Enter age :')
        employeeCountry = raw_input('Enter Country :')
        db.Employees.insert_one({"id": employeeId,"name":employeeName,"age":employeeAge,"country":employeeCountry})
        print '\nInserted data successfully\n'
    except Exception,e:
        print str(e)
        
