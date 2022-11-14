from tkinter import *

import string
from tkinter import messagebox
import subprocess
import pymongo
from datetime import date
from outgoingManagement import outgoingManagement


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]


def outgoingUI():

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

    Label(root,text ="Outgoing Inventory Management", font = 'arial 18 bold', fg="#AE275F", bg="#FFFFFF").place(x=500,y=110)

    ProductID = Entry(root, textvariable = m1 ,width ='80')
    Label(root,text ="Product ID", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=170)
    ProductID.place(x=446,y=170)

    Quantity = Entry(root, textvariable = m2 ,width ='80')
    Label(root,text ="Quantity", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=220)
    Quantity.place(x=446,y=220)

    BuyerName = Entry(root, textvariable = m3 ,width ='80')
    Label(root,text ="BuyerName", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=270)
    BuyerName.place(x=446,y=270)


    def SubmitFunc():
        pid = ProductID.get()
        quan = Quantity.get()
        buynam = BuyerName.get()
        

        output = outgoingManagement(pid, quan, buynam)
        print(output)
        

        accentLabel=Label(root, text=output, fg="#AE275F",bg="#FFFFFF", font="arial 19 bold")
        accentLabel.place(x=550, y=550)

        if (output != "Insufficient Quantity in Inventory!") and (output != "Product is unavailable in Inventory!"):
            messagebox.showinfo("Done!", "Sell order executed")
            root.destroy()

        
        
        
    Button(root, text = "Submit", font = 'arial 15 bold' , command = SubmitFunc ,width = '6', bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=470,y=600)


    root.mainloop()
