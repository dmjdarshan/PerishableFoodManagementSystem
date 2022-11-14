from tkinter import *

import string
from tkinter import messagebox
import subprocess
import pymongo
from datetime import date
from addNewSpace import addNewSpace


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]


def addNewUI():
    root = Tk()
    root.geometry("1383x768")
    root.configure(bg='#FFFFFF')
    root.title("Perishable Food Management System")


    m1 = StringVar()
    m2 = StringVar()
    m3 = StringVar()


    frame1=LabelFrame(root, padx=546, pady=17, bg="#AE275F")
    frame1.place(x=0, y=0)
    Label(frame1, text = "Perishable Food Management System", font = "arial 22 bold",bg="#AE275F" ,fg='#FFFFFF').pack()

    Label(root,text ="Add New Space", font = 'arial 18 bold', fg="#AE275F", bg="#FFFFFF").place(x=500,y=110)

    ProductID = Entry(root, textvariable = m1 ,width ='80')
    Label(root,text ="Product ID", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=165)


    ProductID.place(x=446,y=170)

    ProductName = Entry(root, textvariable = m2 ,width ='80')

    Label(root,text ="Product Name", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=205)
    ProductName.place(x=446,y=210)


    Quantity = Entry(root, textvariable = m3 ,width ='80')
    Label(root,text ="Quantity", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=292)
    Quantity.place(x=446,y=300)

    def SubmitFunc():
        pid = ProductID.get()
        pname = ProductName.get()
        quan = Quantity.get()
        

        output = addNewSpace(pid, pname, quan)
        
        
        messagebox.showinfo("Done!", "Added new space!")
        root.destroy()
        accentLabel=Label(root, text=output, fg="#AE275F",bg="#FFFFFF", font="arial 19 bold")
        accentLabel.place(x=550, y=550)
        



    
        
        
        
    Button(root, text = "Submit", font = 'arial 15 bold' , command = SubmitFunc ,width = '6', bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=470,y=600)


    root.mainloop()
