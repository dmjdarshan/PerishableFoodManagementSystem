import pymongo
from datetime import date
import dayDifference


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]
remainderTable = database["SmartReminder"]


def batchManagement():
    for x in stockTable.find():
        current = date.strftime(date.today(), "%d-%m-%Y")

        expiry = x["ExpiryDate"]
        price = int(x["Price"])
        productID = x["ProductID"]
        productName = x["ProductName"]
        quantity = x["Quantity"]
        batchNo = x["BatchNo"]

        if(abs(dayDifference.numberOfDays(dayDifference.Date(current), dayDifference.Date(expiry))) <= 1):
            print("Entered first")
            stockTable.delete_one(x)

            transactionTable.insert_one({
                "ProductID": productID,
                "BatchNo": batchNo,
                "Quantity": quantity,
                "Price": price,
                "InDate": date.today().strftime("%d-%m-%Y"),
                "OutDate": "",
                "Status": "WASTE"
            })

        if(abs(dayDifference.numberOfDays(dayDifference.Date(current), dayDifference.Date(expiry))) <= 7):
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


if __name__ == "__main__":
    batchManagement()
