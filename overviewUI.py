from tkinter import *

import string
from tkinter import messagebox
import subprocess
import pymongo
from datetime import date
from incomingInventoryManagement import incomingInventoryManagement


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]
remainderTable = database["SmartReminder"]



def overview():
    root = Tk()


    root.geometry("1920x1100")
    root.configure(bg='#FFFFFF')
    root.title("Perishable Food Management System")
    frame1=LabelFrame(root, padx=546, pady=17, bg="#AE275F")
    frame1.place(x=0, y=0)
    Label(frame1, text = "Perishable Food Management System", font = "arial 22 bold",bg="#AE275F" ,fg='#FFFFFF').pack()

    Label(root,text ="Overview", font = 'arial 20 bold',  fg="#AE275F", bg="#FFFFFF").place(x=600,y=80)
 


    can=Canvas(root, width=1300, height=800, bg="#AE275F")
    can.place(x=20, y=120)
    # scrollbar = Scrollbar(can)
    # scrollbar.pack( fill = Y ,side = RIGHT )

    Label(can, text="Stock",bg="#AE275F",fg="#FFFFFF", font="arial 19 bold").place(x=550, y=7)


    y = 90
    Label(can, text="BatchNo" +" - "+ "ProductID"+" - "+'ProductName'+" - "+'Quantity' + " - " +'ExpiryDate',bg="#AE275F",fg="#FFFFFF", font="arial 13 bold").place(x=400, y= 60)
    for x in stockTable.find():
        Label(can, text=x['BatchNo'] +" - "+ x['ProductID']+" - "+x['ProductName']+" - "+x['Quantity'] + " - " +x['ExpiryDate'],bg="#AE275F",fg="#FFFFFF", font="arial 16 bold").place(x=450, y= y+5)
        y = y+35



    root.mainloop()







