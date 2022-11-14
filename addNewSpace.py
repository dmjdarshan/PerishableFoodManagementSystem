import pymongo
from datetime import date
import dayDifference


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
quantityTable = database["Quantity"]

productID, productName, maxQuantity = "","",0

def addNewSpace(productID, productName, maxQuantity):
   

    quantityTable.insert_one({
        "ProductID" : productID,
        "ProductName": productName,
        "MaxQuantity": maxQuantity
    })
    print("Successfully added new Space!")
    return "Successfully added new Space!"
