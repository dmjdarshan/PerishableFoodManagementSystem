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


def incomingUI():
    root = Tk()
    root.geometry("1383x768")
    root.configure(bg='#FFFFFF')
    root.title("Perishable Food Management System")


    m1 = StringVar()
    m2 = StringVar()
    m3 = StringVar()
    m4 = StringVar()
    m5 = StringVar()
    m6 = StringVar()

    frame1=LabelFrame(root, padx=546, pady=17, bg="#AE275F")
    frame1.place(x=0, y=0)
    Label(frame1, text = "Perishable Food Management System", font = "arial 22 bold",bg="#AE275F" ,fg='#FFFFFF').pack()

    Label(root,text ="Incoming Inventory Management", font = 'arial 18 bold', fg="#AE275F", bg="#FFFFFF").place(x=500,y=110)

    ProductID = Entry(root, textvariable = m1 ,width ='80')
    Label(root,text ="Product ID", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=165)


    ProductID.place(x=446,y=170)

    ProductName = Entry(root, textvariable = m2 ,width ='80')

    Label(root,text ="Product Name", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=205)
    ProductName.place(x=446,y=210)

    SellerName = Entry(root, textvariable = m3 ,width ='80')
    Label(root,text ="Seller Name", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=252)
    SellerName.place(x=446,y=260)

    Quantity = Entry(root, textvariable = m4 ,width ='80')
    Label(root,text ="Quantity", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=292)
    Quantity.place(x=446,y=300)

    Price = Entry(root, textvariable = m5 ,width ='80')
    Label(root,text ="Price", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=345)
    Price.place(x=446,y=350)

    ExpiryDate = Entry(root, textvariable = m6 ,width ='80')
    Label(root,text ="Expiry Date", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=385)
    ExpiryDate.place(x=446,y=390)

    def SubmitFunc():
        pid = ProductID.get()
        pname = ProductName.get()
        sname = SellerName.get()
        quan = Quantity.get()
        pric = Price.get()
        expdat = ExpiryDate.get()

        output = incomingInventoryManagement(pid, pname, sname, quan, pric, expdat)
        
        if output == "Successfully Order has been Executed!":
            messagebox.showinfo("Done!", "Buy Order Executed!")
            root.destroy()

        accentLabel=Label(root, text=output, fg="#AE275F",bg="#FFFFFF", font="arial 19 bold")
        accentLabel.place(x=550, y=550)


    
        
        
        
    Button(root, text = "Submit", font = 'arial 15 bold' , command = SubmitFunc ,width = '6', bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=470,y=600)


    root.mainloop()
