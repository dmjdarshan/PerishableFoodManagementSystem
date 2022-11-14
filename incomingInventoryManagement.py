import pymongo
from datetime import date


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]


def incomingInventoryManagement(productSerial, productName, sellerName, quantity, price, expiryDate):

  batchNo, inDate,existingQuantity = 0,"",  0

  # productSerial = "VG501"

  serialFind = stockTable.find({"ProductID":productSerial})
  quantityFind = quantityTable.find({"ProductID":productSerial})

  checkSerialFind = list(serialFind)

  if (len(checkSerialFind) == 0):  #check if product doesnt exist
    batchNo = 1
  else:
    for x in stockTable.find({"ProductID":productSerial}):
      batchNo = int(x['BatchNo'])
      print("test")
      existingQuantity = existingQuantity + int(x['Quantity'])
    batchNo = batchNo + 1
    print(existingQuantity)
    print(batchNo)

  for x in quantityFind:
    maxQuantity = int(x['MaxQuantity'])

  print(maxQuantity)

  if int(existingQuantity) + int(quantity) < maxQuantity:
    print("Inserting into DB")
    stockTable.insert_one({
      "ProductID": productSerial,
      "ProductName": productName,
      "BatchNo" : str(batchNo),
      "SellerName" : sellerName,
      "Quantity" : quantity,
      "Price": price,
      "InDate" : date.today().strftime('%d-%m-%Y'),
      "ExpiryDate": expiryDate
    })
    transactionTable.insert_one({
      "ProductID": productSerial,
      "BatchNo" : batchNo,
      "Quantity" : quantity,
      "Price": price,
      "InDate" : date.today().strftime('%d-%m-%Y'),
      "OutDate": "",
      "Status" : "Buy"
    })
    return ("Successfully Order has been Executed!")

  else:
    print("Warehouse Full")
    return("Warehouse Full!!")


# if __name__ == "__main__":   
#   incomingInventoryManagement()