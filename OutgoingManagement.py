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
    productName, productSerial, batchNo, buyerName, quantity, price, inDate, expiryDate, requiredQuantity = "", "", 0, "", "", "", "", "", 0
    bufferBatchDictionary = []
    availableQuantity = 0

    productSerial = "SN454"

    # productFind = stockTable.find({"ProductID": productSerial})

    if(len(list(stockTable.find({"ProductID": productSerial}))) != 0):
        for x in stockTable.find({"ProductID": productSerial}):
            availableQuantity = availableQuantity+int(x["Quantity"])

        if(availableQuantity >= requiredQuantity):
            for x in stockTable.find({"ProductID": productSerial}):
                if(int(x["Quantity"]) >= requiredQuantity):
                    bufferQuantity = int(x["Quantity"])-requiredQuantity
                    if (bufferQuantity == 0):

                        transactionTable.insert_one({
                            "ProductID": productSerial,
                            "BatchNo": x['BatchNo'],
                            "Quantity": x['Quantity'],
                            "Price": x['Price'],
                            "InDate": "",
                            "OutDate": date.today().strftime("%d-%m-%Y"),
                            "Status": "SELL"
                        })
                        bufferBatchDictionary.append(
                            {'BatchNo': x['BatchNo'], 'Quantity': x['Quantity']})

                        stockTable.delete_one(x)
                    else:
                        transactionTable.insert_one({
                            "ProductID": productSerial,
                            "BatchNo": x['BatchNo'],
                            "Quantity": requiredQuantity,
                            "Price": x['Price'],
                            "InDate": "",
                            "OutDate": date.today().strftime("%d-%m-%Y"),
                            "Status": "SELL"
                        })
                        bufferBatchDictionary.append(
                            {'BatchNo': x['BatchNo'], 'Quantity': x['Quantity']})

                        stockTable.update_one(
                            {"Quantity": int(x["Quantity"])}, {"$set": {"Quantity": bufferQuantity}})
                else:
                    requiredbufferQuantity = abs(
                        int(x["Quantity"])-requiredQuantity)
                    bufferBatchDictionary.append(
                        {'BatchNo': x['BatchNo'], 'Quantity': x['Quantity']})
                    transactionTable.insert_one({
                        "ProductID": productSerial,
                        "BatchNo": x['BatchNo'],
                        "Quantity": x['Quantity'],
                        "Price": x['Price'],
                        "InDate": "",
                        "OutDate": date.today().strftime("%d-%m-%Y"),
                        "Status": "SELL"
                    })
                    # one is batch is deleted but order is not satisfied
                    stockTable.delete_one(x)
            for i in bufferBatchDictionary:
                print("the required order came from the batch number",
                      i["BatchNo"], "and total quantity is ", i["Quantity"])

        else:
            print("Cant satisfy the required quantity")

    else:
        print("This product doesnot exist")


if __name__ == "__main__":
    outgoiningManagement()

    # if(quantityFind > quantity):
    #     for x in productFind:
    #         batch = int(x["BatchNo"])
    #         bufferQuantity = int(x["Quantity"])

    #         if(int(x["Quantity"]) >= requiredQuantity):
    #             buffer = bufferQuantity-requiredQuantity
    #             stockTable.update_one(
    #                 {"Quantity": bufferQuantity}, {"$set": {"Quantity": buffer}})
    #             transactionTable.update_one(
    #                 {"Quantity": bufferQuantity}, {"$set": {"Quantity": buffer}})
    #         else:


# for x in productFind:
    #     productID = int(x["ProductID"])

    # # quantity find and product find vlaues

    # if(productID != productSerial):
    #     print("this product doesnot exist")
    # else:
