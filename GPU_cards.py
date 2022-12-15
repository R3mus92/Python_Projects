import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import ttk

import mysql.connector as mysql

def insert():
    gpu_id = e_gpu_id.get()
    manufacturer = e_manufacturer.get()
    model = e_model.get()
    memory = e_memory.get()
    power_consumption = e_power_consumption.get()
    price = e_price.get()

    if(manufacturer == "" or model == "" or memory == "" or power_consumption == "" or price == ""):
        MessageBox.showinfo("Insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="gpu_cards")
        cursor = con.cursor()
        cursor.execute("insert into gpu values ('" + gpu_id +"','" + manufacturer +"','" + model +"','" + memory +"','" + power_consumption +"','" + price +"')")
        cursor.execute("commit")

        e_gpu_id.delete(0, 'end')
        e_manufacturer.delete(0, 'end')
        e_model.delete(0, 'end')
        e_memory.delete(0, 'end')
        e_power_consumption.delete(0, 'end')
        e_price.delete(0, 'end')

        MessageBox.showinfo("Insert status", "Inserted succesfully")


def show():
    new_window = Toplevel(root)
    new_window.title("GPU Cards List")
    new_window.geometry("1300x500")

    con = mysql.connect(host="localhost", user="root", password="r3musica", database="gpu_cards")
    cursor = con.cursor()
    cursor.execute("select * from gpu")

    gpu = ttk.Treeview(new_window)
    gpu['show'] = 'headings'

    s = ttk.Style(new_window)
    s.theme_use("clam")

    s.configure(".", font=("Helvetica", 8))
    s.configure("Treeview Heading", foreground='red', font=('Helvetica', 11, 'bold'))

    gpu["columns"] = ("gpu_id", "manufacturer", "model", "memory", "power_consumption", "price")

    gpu.column("gpu_id", width=100, minwidth=50, anchor=tkinter.CENTER)
    gpu.column("manufacturer", width=150, minwidth=50, anchor=tkinter.CENTER)
    gpu.column("model", width=150, minwidth=50, anchor=tkinter.CENTER)
    gpu.column("memory", width=150, minwidth=50, anchor=tkinter.CENTER)
    gpu.column("power_consumption", width=150, minwidth=50, anchor=tkinter.CENTER)
    gpu.column("price", width=150, minwidth=50, anchor=tkinter.CENTER)


    gpu.heading("gpu_id", text="GPU Id", anchor=tkinter.CENTER)
    gpu.heading("manufacturer", text="Manufacturer", anchor=tkinter.CENTER)
    gpu.heading("model", text="Model", anchor=tkinter.CENTER)
    gpu.heading("memory", text="Memory (GB)", anchor=tkinter.CENTER)
    gpu.heading("power_consumption", text="Power consumption (W)", anchor=tkinter.CENTER)
    gpu.heading("price", text="Price(EUR)", anchor=tkinter.CENTER)



    i=0
    for row in cursor:
        gpu.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        i = i + 1
    Label(new_window, text="Available GPU Cards")
    gpu.pack()


def get_by_id():
    if(e_gpu_id.get()==""):
        MessageBox.showinfo("Insert status", "ID field is required")
    else:
        new_window = Toplevel(root)
        new_window.title("GPU Cards List")
        new_window.geometry("1300x500")

        con = mysql.connect(host="localhost", user="root", password="r3musica", database="gpu_cards")
        cursor = con.cursor()
        cursor.execute("select * from gpu where gpu_id='"+e_gpu_id.get()+"'")


        gpu = ttk.Treeview(new_window)
        gpu['show'] = 'headings'

        s = ttk.Style(new_window)
        s.theme_use("clam")

        s.configure(".", font=("Helvetica", 8))
        s.configure("Treeview Heading", foreground='red', font=('Helvetica', 11, 'bold'))

        gpu["columns"] = ("gpu_id", "manufacturer", "model", "memory", "power_consumption", "price")

        gpu.column("gpu_id", width=100, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("manufacturer", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("model", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("memory", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("power_consumption", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("price", width=150, minwidth=50, anchor=tkinter.CENTER)


        gpu.heading("gpu_id", text="GPU Id", anchor=tkinter.CENTER)
        gpu.heading("manufacturer", text="Manufacturer", anchor=tkinter.CENTER)
        gpu.heading("model", text="Model", anchor=tkinter.CENTER)
        gpu.heading("memory", text="Memory (GB)", anchor=tkinter.CENTER)
        gpu.heading("power_consumption", text="Power consumption (W)", anchor=tkinter.CENTER)
        gpu.heading("price", text="Price(EUR)", anchor=tkinter.CENTER)



        i=0
        for row in cursor:
            gpu.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        Label(new_window, text="Available GPU Cards")
        gpu.pack()

def get_by_manuf():
    if(e_manufacturer.get()==""):
        MessageBox.showinfo("Insert status", "Manufacturer field is required")
    else:
        new_window = Toplevel(root)
        new_window.title("GPU Cards List")
        new_window.geometry("1300x500")

        con = mysql.connect(host="localhost", user="root", password="r3musica", database="gpu_cards")
        cursor = con.cursor()
        cursor.execute("select * from gpu where manufacturer='"+e_manufacturer.get()+"'")


        gpu = ttk.Treeview(new_window)
        gpu['show'] = 'headings'

        s = ttk.Style(new_window)
        s.theme_use("clam")

        s.configure(".", font=("Helvetica", 8))
        s.configure("Treeview Heading", foreground='red', font=('Helvetica', 11, 'bold'))

        gpu["columns"] = ("gpu_id", "manufacturer", "model", "memory", "power_consumption", "price")

        gpu.column("gpu_id", width=100, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("manufacturer", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("model", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("memory", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("power_consumption", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("price", width=150, minwidth=50, anchor=tkinter.CENTER)


        gpu.heading("gpu_id", text="GPU Id", anchor=tkinter.CENTER)
        gpu.heading("manufacturer", text="Manufacturer", anchor=tkinter.CENTER)
        gpu.heading("model", text="Model", anchor=tkinter.CENTER)
        gpu.heading("memory", text="Memory (GB)", anchor=tkinter.CENTER)
        gpu.heading("power_consumption", text="Power consumption (W)", anchor=tkinter.CENTER)
        gpu.heading("price", text="Price(EUR)", anchor=tkinter.CENTER)



        i=0
        for row in cursor:
            gpu.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        Label(new_window, text="Available GPU Cards")
        gpu.pack()

def get_by_memory():
    if(e_memory.get()==""):
        MessageBox.showinfo("Insert status", "Memory field is required")
    else:
        new_window = Toplevel(root)
        new_window.title("GPU Cards List")
        new_window.geometry("1300x500")

        con = mysql.connect(host="localhost", user="root", password="r3musica", database="gpu_cards")
        cursor = con.cursor()
        cursor.execute("select * from gpu where memory='"+e_memory.get()+"'")


        gpu = ttk.Treeview(new_window)
        gpu['show'] = 'headings'

        s = ttk.Style(new_window)
        s.theme_use("clam")

        s.configure(".", font=("Helvetica", 8))
        s.configure("Treeview Heading", foreground='red', font=('Helvetica', 11, 'bold'))

        gpu["columns"] = ("gpu_id", "manufacturer", "model", "memory", "power_consumption", "price")

        gpu.column("gpu_id", width=100, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("manufacturer", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("model", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("memory", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("power_consumption", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("price", width=150, minwidth=50, anchor=tkinter.CENTER)


        gpu.heading("gpu_id", text="GPU Id", anchor=tkinter.CENTER)
        gpu.heading("manufacturer", text="Manufacturer", anchor=tkinter.CENTER)
        gpu.heading("model", text="Model", anchor=tkinter.CENTER)
        gpu.heading("memory", text="Memory (GB)", anchor=tkinter.CENTER)
        gpu.heading("power_consumption", text="Power consumption (W)", anchor=tkinter.CENTER)
        gpu.heading("price", text="Price(EUR)", anchor=tkinter.CENTER)



        i=0
        for row in cursor:
            gpu.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        Label(new_window, text="Available GPU Cards")
        gpu.pack()


def get_by_power():
    if(e_power_consumption.get()==""):
        MessageBox.showinfo("Insert status", "Power field is required")
    else:
        new_window = Toplevel(root)
        new_window.title("GPU Cards List")
        new_window.geometry("1300x500")

        con = mysql.connect(host="localhost", user="root", password="r3musica", database="gpu_cards")
        cursor = con.cursor()
        cursor.execute("select * from gpu where power_consumption='"+e_power_consumption.get()+"'")


        gpu = ttk.Treeview(new_window)
        gpu['show'] = 'headings'

        s = ttk.Style(new_window)
        s.theme_use("clam")

        s.configure(".", font=("Helvetica", 8))
        s.configure("Treeview Heading", foreground='red', font=('Helvetica', 11, 'bold'))

        gpu["columns"] = ("gpu_id", "manufacturer", "model", "memory", "power_consumption", "price")

        gpu.column("gpu_id", width=100, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("manufacturer", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("model", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("memory", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("power_consumption", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("price", width=150, minwidth=50, anchor=tkinter.CENTER)


        gpu.heading("gpu_id", text="GPU Id", anchor=tkinter.CENTER)
        gpu.heading("manufacturer", text="Manufacturer", anchor=tkinter.CENTER)
        gpu.heading("model", text="Model", anchor=tkinter.CENTER)
        gpu.heading("memory", text="Memory (GB)", anchor=tkinter.CENTER)
        gpu.heading("power_consumption", text="Power consumption (W)", anchor=tkinter.CENTER)
        gpu.heading("price", text="Price(EUR)", anchor=tkinter.CENTER)



        i=0
        for row in cursor:
            gpu.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        Label(new_window, text="Available GPU Cards")
        gpu.pack()


def get_by_price():
    if(e_price.get()==""):
        MessageBox.showinfo("Insert status", "Price field is required")
    else:
        new_window = Toplevel(root)
        new_window.title("GPU Cards List")
        new_window.geometry("1300x500")

        con = mysql.connect(host="localhost", user="root", password="r3musica", database="gpu_cards")
        cursor = con.cursor()
        cursor.execute("select * from gpu where price='"+e_price.get()+"'")


        gpu = ttk.Treeview(new_window)
        gpu['show'] = 'headings'

        s = ttk.Style(new_window)
        s.theme_use("clam")

        s.configure(".", font=("Helvetica", 8))
        s.configure("Treeview Heading", foreground='red', font=('Helvetica', 11, 'bold'))

        gpu["columns"] = ("gpu_id", "manufacturer", "model", "memory", "power_consumption", "price")

        gpu.column("gpu_id", width=100, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("manufacturer", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("model", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("memory", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("power_consumption", width=150, minwidth=50, anchor=tkinter.CENTER)
        gpu.column("price", width=150, minwidth=50, anchor=tkinter.CENTER)


        gpu.heading("gpu_id", text="GPU Id", anchor=tkinter.CENTER)
        gpu.heading("manufacturer", text="Manufacturer", anchor=tkinter.CENTER)
        gpu.heading("model", text="Model", anchor=tkinter.CENTER)
        gpu.heading("memory", text="Memory (GB)", anchor=tkinter.CENTER)
        gpu.heading("power_consumption", text="Power consumption (W)", anchor=tkinter.CENTER)
        gpu.heading("price", text="Price(EUR)", anchor=tkinter.CENTER)



        i=0
        for row in cursor:
            gpu.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1
        Label(new_window, text="Available GPU Cards")
        gpu.pack()



root = Tk()
root.geometry("1000x600")
root.title("GPU Cards Inventory")

gpu_id = Label(root, text='Enter ID', font=('bold', 12))
gpu_id.place(x=20, y=30)

manufacturer = Label(root, text='Enter manufacturer', font=('bold', 12))
manufacturer.place(x=20, y=60)

model = Label(root, text='Enter model', font=('bold', 12))
model.place(x=20, y=90)

memory = Label(root, text='Enter memory (GB)', font=('bold', 12))
memory.place(x=20, y=120)


power_consumption = Label(root, text='Enter power consumption (W)', font=('bold', 12))
power_consumption.place(x=20, y=150)

price = Label(root, text='Enter price (EUR)', font=('bold', 12))
price.place(x=20, y=180)



e_gpu_id = Entry()
e_gpu_id.place(x=300, y=30)

e_manufacturer = Entry()
e_manufacturer.place(x=300, y=60)

e_model = Entry()
e_model.place(x=300, y=90)

e_memory = Entry()
e_memory.place(x=300, y=120)

e_power_consumption = Entry()
e_power_consumption.place(x=300, y=150)

e_price = Entry()
e_price.place(x=300, y=180)

insert = Button(root, text="Insert into GPU list", font=("italic", 10), bg="White", command=insert)
insert.place(x=50, y=300)

show = Button(root, text="Show GPU list", font=("italic", 10), bg="White", command=show)
show.place(x=180, y=300)

get = Button(root, text="Search GPU list by ID", font=("italic", 10), bg="White", command=get_by_id)
get.place(x=450, y=30)

get = Button(root, text="Search GPU list by manufacturer", font=("italic", 10), bg="White", command=get_by_manuf)
get.place(x=450, y=60)

get = Button(root, text="Search GPU list by memory", font=("italic", 10), bg="White", command=get_by_memory)
get.place(x=450, y=120)

get = Button(root, text="Search GPU list by power consumption", font=("italic", 10), bg="White", command=get_by_power)
get.place(x=450, y=150)

get = Button(root, text="Search GPU list by price", font=("italic", 10), bg="White", command=get_by_price)
get.place(x=450, y=180)



#     gpu_id = e_gpu_id.get()
#     manufacturer = e_manufacturer.get()
#     model = e_model.get()
#     memory = e_memory.get()
#     power_consumption = e_power_consumption.get()
#     price = e_price.get()



# insert = Button(root, text="Insert",font=("Italic",12), bg="White", command=insert)



root.mainloop()