#Created by: Benjamin Mapesa (Mapesa254)
#My first Tkinter project using structured programming
#A basic log in page
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from os import sys

#Creating the root page
root = Tk()
#Setting the title of the page
root.title('LOGIN PAGE')
#Setting the size of the page
root.geometry('800x600')

#Using event handling concept to configure the login button command
#Also utilisation of the message box from tkinter module
def login():
    account = account_number.get()
    password = pasword_digits.get()
    #Used a sample input data to test code functionality
    if account == '12345678' and password == 'mypass254':
        messagebox.showinfo('Success', 'Login successful') 
        sys.exit() 
    else:
        messagebox.showerror('Error', 'Invalid account number or password')

#Creating the  main label and additional label
message = Label(root,text='WELCOME TO 254 ONLINE BANKING',  fg ='purple', font =('Arial bold', '25'))
instructions = Label(root, text='Enter your details in the provided fields', fg ='blue', font = ('New Times bold', '12'))
#Setting the position of the labels
message.place(x=100 ,y=40)
instructions.place(x=110, y=160)

#Creating the Account Number and password labels, entry fields and log in button
account_label = Label(root, text='Account number', font=('Arial bold', '16'))
account_number = Entry(root, font=('Arial', '16'),  )
password_label = Label(root, text='Password',  font=('Arial bold', '16'))
pasword_digits = Entry(root,  show='*', font=('Arial', '16'))
login_button = Button(root, text='LOGIN', font=('Arial bold', '16' ), command=login)

'''
Setting the position of the Account Number and password labels, 
entry fields and log in button
'''
account_label.place(x=150, y=200)
account_number.place(x=400, y=200)
password_label.place(x=150, y=300)
pasword_digits.place(x=400, y=300)
login_button.place(x=300 , y=400)

#Looping the display window
root.mainloop()
