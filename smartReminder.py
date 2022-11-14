import pymongo
import dayDifference
from datetime import date

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
reminderTable = database["SmartReminder"]

today = date.strftime(date.today(), "%d-%m-%Y")

def smartReminder():
    for reminders in reminderTable.find():
        if (dayDifference.numberOfDays(dayDifference.Date(today), dayDifference.Date(reminders['ExpiryDate'])) < 0):
           print("Deleting reminder") 
           reminderTable.delete_one(reminders)


smartReminder()