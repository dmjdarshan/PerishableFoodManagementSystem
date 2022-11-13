from numpy import product
import pymongo
from datetime import date


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]


def incomingInventoryManagement():

    productName, productSerial, batchNo, sellerName, quantity, price, inDate, expiryDate, existingQuantity = "", "", 0, "", "", "", "", "", 0

    productSerial = "TP100"

    productFind = stockTable.find({"ProductID": productSerial})
    quantityFind = quantityTable.find({"ProductID": productSerial})
    productFindList = list(productFind)

    if(len(productFindList) != 0):

        for x in productFind:
            batchNo = batchNo + 1
            existingQuantity = existingQuantity + int(x['Quantity'])
        batchNo = batchNo + 1

        for x in quantityFind:
            maxQuantity = int(x['ToatalQuantity'])

        if existingQuantity + quantity < maxQuantity:
            print("Inserting into DB")
            stockTable.insert_one({
                "ProductID": productSerial,
                "ProductName": productName,
                "BatchNo": batchNo,
                "SellerName": sellerName,
                "Quantity": quantity,
                "Price": price,
                "InDate": date.today(),
                "ExpiryDate": expiryDate
            })
            transactionTable.insert_one({
                "ProductID": productSerial,
                "BatchNo": batchNo,
                "Quantity": quantity,
                "Price": price,
                "InDate": date.today().strftime("%d-%m-%Y"),
                "OutDate": "",
                "Status": "BUY"
            })

        else:
            print("Warehouse Full")
    else:
        # add new product

        # if __name__ == "__main__":
        #     incomingInventoryManagement()
