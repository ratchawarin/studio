from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkinter import ttk

try:
    conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS register (
        id integer PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        name TEXT,
        phone TEXT,
        home_number TEXT,
        m TEXT,
        s TEXT,
        r TEXT,
        d TEXT,
        dis TEXT,
        pro TEXT,
        pi TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS STD1 (
        id integer PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        month TEXT,
        years TEXT,
        date2 TEXT,
        month2 TEXT,
        years2 TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS STD2 (
        id integer PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        month TEXT,
        years TEXT,
        date2 TEXT,
        month2 TEXT,
        years2 TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS STD3 (
        id integer PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        month TEXT,
        years TEXT,
        date2 TEXT,
        month2 TEXT,
        years2 TEXT
    )
    """)

    conn.commit()
except sqlite3.Error as e:
    messagebox.showerror("Database Error", str(e))

def homePage():
# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')

# Background
    img = Image.open("BG2.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo       # เก็บ reference รูป

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4
    
#login
    Button1 = Button(current_window)
    Button1.place(relx=0.388, rely=0.832 ,width=105, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button login12.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage)
    Button1.image = img5

#rge
    Button1 = Button(current_window)
    Button1.place(relx=0.543, rely=0.832 ,width=143, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img6 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button reg.png")
    Button1.configure(image=img6)
    Button1.configure(command=homePage)
    Button1.image = img6

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7

    current_window.mainloop()
homePage()