from tkinter import *
from tkinter import ttk
from pymongo import MongoClient



def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = ""
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['GUI_App']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
   # Get the database
   dbname = get_database()


# window = Tk()
# window.title(" Database builder ")
# window.geometry('400x400')
# window.configure(background = "white");

# fist_var = StringVar()
# last_var = StringVar()
# email_var = StringVar()
# contact_var = IntVar()


# a = Label(window ,text = "First Name").grid(row = 0,column = 0)
# b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
# c = Label(window ,text = "Email").grid(row = 2,column = 0)
# d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
# a1 = Entry(window, textvariable= fist_var).grid(row = 0,column = 1)
# b1 = Entry(window, textvariable= last_var).grid(row = 1,column = 1)
# c1 = Entry(window, textvariable= email_var).grid(row = 2,column = 1)
# d1 = Entry(window, textvariable= contact_var).grid(row = 3,column = 1)


# def test():
#     first = fist_var.get()
#     last = last_var.get()
#     email = email_var.get()
#     contact = contact_var.get()
#     print(first, last, email, contact)

# button = Button(window, text="Hello", command=(test) )
# button.grid()
# window.mainloop()