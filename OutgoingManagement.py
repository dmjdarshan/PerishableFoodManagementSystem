from errno import ESTALE
import pymongo
from datetime import date


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]
remainderTable = database["SmartReminder"]

bufferBatchDictionary = []


def outgoiningManagement():
    productName, productSerial, batchNo, buyerName, quantity, price, inDate, expiryDate, requiredQuantity = "", "", 0, "", "", "", "", "", 20
    bufferBatchDictionary = []
    availableQuantity = 0

    productSerial = "VG500"

    if(len(list(stockTable.find({"ProductID": productSerial}))) != 0):
        print("product is there")
        for x in stockTable.find({"ProductID": productSerial}):
            availableQuantity = availableQuantity+int(x["Quantity"])
        print("Available Quantity:", availableQuantity)
        if(availableQuantity >= requiredQuantity):
            print("Quantity is there")
            bufferQuantity = requiredQuantity
            while bufferQuantity != 0:
                stockRow = stockTable.find_one({'ProductID': productSerial})
                if (abs(bufferQuantity - int(stockRow['Quantity'])) == 0):
                    bufferQuantity = bufferQuantity - int(stockRow['Quantity'])
                    print("Buffer Quantity:", bufferQuantity)
                    transactionTable.insert_one({
                        "ProductID": productSerial,
                        "BatchNo": stockRow['BatchNo'],
                        "Quantity": stockRow['Quantity'],
                        "Price": stockRow['Price'],
                        "InDate": "",
                        "OutDate": date.today().strftime("%d-%m-%Y"),
                        "Status": "SELL"
                    })
                    bufferBatchDictionary.append(
                        {'BatchNo': stockRow['BatchNo'], 'Quantity': stockRow['Quantity']})
                    print("bufferdictionary:", bufferBatchDictionary)
                    stockTable.delete_one(stockRow)
                else:
                    if (bufferQuantity - int(stockRow['Quantity']) < 0):
                        temp = abs(bufferQuantity - int(stockRow['Quantity']))

                        transactionTable.insert_one({
                            "ProductID": productSerial,
                            "BatchNo": stockRow['BatchNo'],
                            "Quantity": stockRow['Quantity'],
                            "Price": stockRow['Price'],
                            "InDate": "",
                            "OutDate": date.today().strftime("%d-%m-%Y"),
                            "Status": "SELL"
                        })
                        bufferBatchDictionary.append(
                            {'BatchNo': stockRow['BatchNo'], 'Quantity': bufferQuantity})
                        bufferQuantity = 0
                        print("bufferdictionary:", bufferBatchDictionary)

                        stockTable.update_one({"BatchNo": stockRow['BatchNo'], "ProductID": productSerial}, {
                                              "$set": {"Quantity": str(temp)}})

                    else:
                        bufferQuantity = bufferQuantity - \
                            int(stockRow['Quantity'])
                        print("Buffer Quantity:", bufferQuantity)
                        transactionTable.insert_one({
                            "ProductID": productSerial,
                            "BatchNo": stockRow['BatchNo'],
                            "Quantity": stockRow['Quantity'],
                            "Price": stockRow['Price'],
                            "InDate": "",
                            "OutDate": date.today().strftime("%d-%m-%Y"),
                            "Status": "SELL"
                        })
                        bufferBatchDictionary.append(
                            {'BatchNo': stockRow['BatchNo'], 'Quantity': stockRow['Quantity']})
                        print("bufferdictionary:", bufferBatchDictionary)
                        stockTable.delete_one(stockRow)
            print(bufferBatchDictionary)
        else:
            print("Not enough Quantity")
    else:
        print("Product is unavailable")


if __name__ == "__main__":
    outgoiningManagement()
