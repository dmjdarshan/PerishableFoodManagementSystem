import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]

def fun():
    for x in stockTable.find():
        print(x['ProductName'])
    
    for x in stockTable.find({'ProductID' : "TP100"}):
        print(x['ProductName'])


fun()