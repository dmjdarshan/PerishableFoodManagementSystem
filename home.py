from tkinter import *

import string
from tkinter import messagebox
import subprocess
import pymongo
from datetime import date
from incomingInventoryManagement import incomingInventoryManagement
from smartReminder import smartReminder
from IncomingUI import incomingUI
from outgoingUI import outgoingUI
from addNewUI import addNewUI
from batchManagement import batchManagement
from overviewUI import overview

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]
remainderTable = database["SmartReminder"]



def home():
    root = Tk()


    root.geometry("1920x1100")
    root.configure(bg='#FFFFFF')
    root.title("Perishable Food Management System")
    frame1=LabelFrame(root, padx=546, pady=17, bg="#AE275F")
    frame1.place(x=0, y=0)
    Label(frame1, text = "Perishable Food Management System", font = "arial 22 bold",bg="#AE275F" ,fg='#FFFFFF').pack()

    Label(root,text ="Home", font = 'arial 20 bold',  fg="#AE275F", bg="#FFFFFF").place(x=650,y=80)
    def iim():
        print("hii")
        incomingUI()

    def oim():
        print("hii")
        outgoingUI()

    def addnew():
        addNewUI()

    def overw():
        print("hi")
        overview()

    def refre():
        smartReminder() 
        batchManagement()
         



    Button(root, text = "Incoming Inventory Management", font = 'arial 15 bold' , width="30", command = iim , bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=10,y=180)
    Button(root, text = "Overview", font = 'arial 15 bold' , width="15", command = overw , bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=390,y=180)
    Button(root, text = "Outgoing Inventory Management", font = 'arial 15 bold' , width="30", command = oim , bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=600,y=180)
    Button(root, text = "Add New", font = 'arial 15 bold' , width="30", command = addnew , bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=980,y=180)

    Button(root, text = "Refresh", font = 'arial 15 bold' , width="30", command = refre , bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=500,y=250)



    can=Canvas(root, width=1900, height=800, bg="#AE275F")
    can.place(x=0, y=300)
    # scrollbar = Scrollbar(can)
    # scrollbar.pack( fill = Y ,side = RIGHT )

    Label(can, text="Smart Reminders",bg="#AE275F",fg="#FFFFFF", font="arial 19 bold").place(x=550, y=7)


    y = 50

    for x in remainderTable.find():
        Label(can, text=x['ProductID']+" - "+x['ProductName']+" expires on "+x['ExpiryDate'],bg="#AE275F",fg="#FFFFFF", font="arial 16 bold").place(x=450, y= y+5)
        y = y+35



    root.mainloop()








