import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Perishable_food_management_system"]
mycol = mydb["Stock"]

cur = mycol.find()

results = list(cur)

# Checking the cursor is empty
# or not
if len(results) == 0:
    print("Empty Cursor")
else:
    print("Cursor is Not Empty")
    print("Do Stuff Here")


# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Perishable_food_management_system"]
# mycol = mydb["Stock"]


# def BatchManagement():


# for x in mycol.find({}, {"_id": 0, "ProductID": 1}):
#     print(max(x.get("ProductID"))

# x = mycol.find_one()
