from tkinter import *
from tkinter import ttk
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["items"]

window = Tk()
window.title(" Database builder ")
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
treeviews.insert('', 0, 'Fullname', text='Yes', values=("Luis Abreu", "luis1abreu@gmail.com", "3476616555"))
treeviews.insert('', 0, 'test', text='Yes', values=("ASbreu", "luis@gmail.com", "34763433555"))


def submit():
    first = fist_var.get()
    last = last_var.get()
    email = email_var.get()
    contact = contact_var.get()

    item_2 = {
      "_id" : "U1IT00022",
      "Name" : first + " " + last,
      "email" : email,
      "Contact" : contact,
   }
    collection_name.insert_one(item_2)

button = Button(window, text="Hello", command=(submit))
button.grid(row=4, column=0)
window.mainloop()