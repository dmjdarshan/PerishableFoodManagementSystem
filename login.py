import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
loginTable = database["Login"]

# username, password = "Adithya", "Adiadi123"


def Login(username, password):
    for x in loginTable.find({"UserName": username}):
        if(len(list(loginTable.find({"UserName": username}))) != 0):
            if(x["UserName"] == username):
                if(x["Password"] == password):
                    print("ACCESS GRANTED")
                    return("ACCESS GRANTED")
                else:
                    print("INVALID PASSWORD")
                    return("INVALID PASSWORD/USERNAME")
        else:
            print("ACCESS DENIED")
            return("ACCESS DENIED")


if __name__ == "__main__":
    Login()