from tkinter import *

import string
from tkinter import messagebox
import subprocess
import pymongo
from datetime import date
from login import Login
from home import home


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Perishable_food_management_system"]
stockTable = database["Stock"]
quantityTable = database["Quantity"]
transactionTable = database["Transaction"]


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

Label(root,text ="Login", font = 'arial 18 bold', fg="#AE275F", bg="#FFFFFF").place(x=550,y=110)

Username = Entry(root, textvariable = m1 ,width ='40')
Label(root,text ="Username", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=165)


Username.place(x=446,y=170)

Password = Entry(root, textvariable = m2 ,width ='40')

Label(root,text ="Password", font = 'arial 15 bold',  fg="#AE275F", bg="#FFFFFF").place(x=300,y=205)
Password.place(x=446,y=210)



def SubmitFunc():
    un = Username.get()
    ps = Password.get()
    

    output = Login(un, ps)

    def enter():
        root.destroy()
        home()
        
    
    if output == "ACCESS GRANTED":
        messagebox.showinfo("Done!", "Welcome!")
        enter()
       


    accentLabel=Label(root, text=output, fg="#AE275F",bg="#FFFFFF", font="arial 19 bold")
    accentLabel.place(x=550, y=550)



   
    
    
    
Button(root, text = "Login", font = 'arial 15 bold' , command = SubmitFunc ,width = '4', bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=500,y=270)


root.mainloop()
