import re
from tkinter import *
from tkinter import ttk
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["items"]


window = Tk()
window.title("Inserting Data :)")
window.geometry('1000x400')
window.configure(background = "white");

fist_var = StringVar()
last_var = StringVar()
email_var = StringVar()
contact_var = IntVar()


a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Email").grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
a1 = Entry(window, textvariable= fist_var).grid(row = 0,column = 1)
b1 = Entry(window, textvariable= last_var).grid(row = 1,column = 1)
c1 = Entry(window, textvariable= email_var).grid(row = 2,column = 1)
d1 = Entry(window, textvariable= contact_var).grid(row = 3,column = 1)


column_name = ("Fullname", "Email Address", "Phone Number")
treeviews = ttk.Treeview(window)
treeviews.configure(columns=column_name)
treeviews.heading("#0", text="Membership")
treeviews.heading("Fullname", text="Fullname")
treeviews.heading("Email Address", text="Email Address")
treeviews.heading("Phone Number", text="Phone Number")
treeviews.grid(row=5, column=1)

treeviews.column("#0", anchor=CENTER)
treeviews.column("Fullname", anchor=CENTER)
treeviews.column("Email Address", anchor=CENTER)
treeviews.column("Phone Number", anchor=CENTER)

def submit():
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  try:
    #Gets information from treeviews form
    first = fist_var.get()
    last = last_var.get()
    email = email_var.get()
    contact = contact_var.get()

    #checks if the form has a valid email if not info will not be inserted
    if(re.fullmatch(regex, email)):
      print("valid Email")
      item_2 = {
        "Name" : first + " " + last,
        "email" : email,
        "Contact" : contact
      }
      db_insert(item_2)
    else:
      print("Invalid Email")
  except Exception as err:
    print(err)

def db_insert(item_2):
  collection_name.insert_one(item_2)
  item_details = collection_name.find()
  for item in item_details:
    treeviews.insert('', 'end', text='Yes', values=(item['Name'], item['email'], item['Contact']))

def db_delete():
  pass

button = Button(window, text="Hello", command=(submit))
button.grid(row=4, column=0)
window.mainloop()