import pymongo
from datetime import date
import dayDifference


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
quantityTable = database["Quantity"]

productID, productName, maxQuantity = "","",0

def addNewSpace():
    #testpurpose
    productID = "SS200"
    productName = "CANDY"
    maxQuantity = 500

    quantityTable.insert_one({
        "ProductID" : productID,
        "ProductName": productName,
        "MaxQuantity": maxQuantity
    })
    print("Inserted Successfully")
