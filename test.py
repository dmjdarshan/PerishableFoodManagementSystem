from errno import ESTALE
import pymongo
from datetime import date


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]
remainderTable = database["SmartReminder"]


def outgoiningManagement():
    productName, productSerial, batchNo, buyerName, quantity, price, inDate, expiryDate, requiredQuantity = "", "", 0, "", "", "", "", "", 50
    bufferBatchDictionary = []
    availableQuantity = 0

    productSerial = "SN454"

    productFind = quantityTable.find({"ProductID": productSerial})
    a = productFind
    if(len(list(productFind)) != 0):
        print("Enter")
        for x in a:
            print("1")
            print(x["Quantity"])
            availableQuantity = availableQuantity+int(x["Quantity"])


outgoiningManagement()
