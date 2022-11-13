import pymongo
from datetime import date


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]
remainderTable = database["Remaider"]


def batchManagement():
    for x in stockTable.find():
        current = date.strptime(date.today(), "%d-%m-%Y")

        expiry = x["ExpiryDate"]
        price = int(x["Price"])
        productID = x["ProductID"]
        productName = x["ProductName"]
        quantity = x["Quantity"]
        batchNo = x["BatchNo"]

        expiry = date.strptime(expiry, "%d-%m-%Y")

        if(abs(expiry-current) <= 1):
            stockTable.delete_one(x)

            transactionTable.insert_one({
                "ProductID": productID,
                "BatchNo": batchNo,
                "Quantity": quantity,
                "Price": price,
                "InDate": date.today(),
                "OutDate": "",
                "Status": "WASTE"
            })

        if(abs(expiry-current) <= 7):
            price = price/2
            stockTable.update_one(
                {"Price": x["Price"]}, {"$set": {"Price": price}})
        else:
            print("give remainder")
            remainderTable.insert_one({
                "ProductID": productID,
                "ProductName": productName,
                "ExpiryDate": expiry
            })

    # expiryFind = stockTable.find({"ExpiryDate"})
    # priceFind = stockTable.find({"Price"})

    # curent = date.strptime(date.today(), "%Y/%m/%d")

    # for x in expiryFind:
    #     expiry = date.strptime(x, "%Y/%m/%d")

    #     if(abs(expiry-curent) <= 1):
    #     {

    #     }

        # if(abs(expiry-curent) <= 7):
        # {
        #     print("yes")
        # }
        # else:
        # print("give remainder")
        # remainderTable.insert_one({
        #     "ProductID": productSerial,
        #     "ProductName": productName,
        # })
