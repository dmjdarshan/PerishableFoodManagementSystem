
import pymongo
from datetime import date


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]


def incomingInventoryManagement():

    productName, productSerial, batchNo, sellerName, quantity, price, inDate, expiryDate, existingQuantity = "", "", 0,"","","","","", 0

    print("Testing")
    productSerial = "TP101"

    serialFind = stockTable.find({"ProductID": productSerial})

    test = list(serialFind)

    if (len(test) == 0):
        print("Product not there")

    for x in serialFind:
        print(x['ProductName'])
    




if __name__ == "__main__":   
  incomingInventoryManagement()




