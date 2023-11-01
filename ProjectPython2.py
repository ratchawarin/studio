from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from tkcalendar import Calendar
import sqlite3
from tkinter import Toplevel, Label, Button
from datetime import datetime
import tkinter as tk


conn = sqlite3.connect("E:/PythonPJ/PythonPJ/khantepStudio1_data.db")
cursor = conn.cursor()

# try:
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS register (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT,
#         password TEXT,
#         name TEXT,
#         IDcard varcher(13) NOT NULL,
#         phone TEXT,
#         home_number TEXT,
#         m TEXT,
#         s TEXT,
#         r TEXT,
#         d TEXT,
#         dis TEXT,
#         pro TEXT,
#         pi TEXT
#     )
#     """)

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS STD1 (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             studio TEXT,
#             date TEXT,
#             time TEXT,
#             status1 TEXT,
#             day TEXT,
#             month TEXT,
#             Year TEXT
                   
            
#         )
#     """)

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS STD2 (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             studio TEXT,
#             date TEXT,
#             time TEXT,
#             status2 TEXT,
#             day TEXT,
#             month TEXT,
#             Year TEXT
           
            
#         )
#     """)

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS STD3 (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             studio TEXT,
#             date TEXT,
#             time TEXT,
#             status3 TEXT,
#             day TEXT,
#             month TEXT,
#             Year TEXT
#         )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS history (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         IDcard  TEXT,
#         phone TEXT,
#         studio TEXT,
#         date TEXT,
#         time NOT NULL
#     )
#     """)

    
    

#     conn.commit()
#     conn.close()
# except sqlite3.Error as e:
#     print("Database Error:", str(e))



currentwindow = None

def registerPage():
    global currentwindow 
    if currentwindow:
        currentwindow.destroy()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('E:\PythonPJ\PythonPJ\KhantepStudio.ico')

    
    def regis():
        
        username = registerEntry.get()
        password = passwordEntry.get()
        name = nameEntry.get()
        idcard = idcardEntry.get()
        phone = telEntry.get()
        home_number = homenbEntry.get()
        m = mEntry.get()
        s = sEntry.get()
        r = rEntry.get()
        d = dEntry.get()
        dis = disEntry.get()
        pro = proEntry.get()
        pi = piEntry.get()
        conn = sqlite3.connect("E:/PythonPJ/PythonPJ/khantepStudio1_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM register WHERE username=?", (username,))
        existing_username = cursor.fetchone()
    # เพิ่มเงื่อนไขตรวจสอบว่ามีช่องใดช่องหนึ่งไม่ได้กรอกข้อมูลเข้าไป
        if not (username and password and idcard and name and phone and home_number and m and s and r and d and dis and pro and pi):
            messagebox.showerror("Error", "กรุณากรอกให้ครบทุกช่อง")
        else:
            conn = sqlite3.connect("E:/PythonPJ/PythonPJ/khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM register WHERE username=?", (username,))
            existing_username = cursor.fetchone()

            if existing_username:
                messagebox.showerror("Error", "มีคนใช้ username นี้ไปแล้ว")
                registerEntry.delete(0,END)
            elif not idcard.isdigit():
                messagebox.showerror("Error", "กรุณากรอกเลขบัตรประชาชนเป็นตัวเลขเท่านั้น")

            elif len(idcard) != 13:
                messagebox.showerror("Error", "เลขบัตรประชาชนควรมี 13 หลัก")

            elif not phone.isdigit():
                messagebox.showerror("Error", "กรุณากรอกเบอร์โทศัพท์ให้ถูกต้อง")
            elif len(phone) != 10:
                messagebox.showerror("Error", "เบอร์โทรศัพท์ควรมี 10 หลัก")

            elif not home_number.isdigit():
                messagebox.showerror("Error", "กรุณากรอกบ้านเลขที่ให้ถูกต้อง")
            elif len(home_number) < 1 or len(home_number) > 3:
                messagebox.showerror("Error", "บ้านเลขที่ไม่เกินควร 3 หลัก")

            elif not m.isdigit():
                messagebox.showerror("Error", "กรุณากรอกเลขที่หมู่บ้านให้ถูกต้อง")
            elif len(m) < 1 or len(m) > 2:
                messagebox.showerror("Error", "เลขที่หมู่บ้านไม่เกินควร 2 หลัก")

            elif not pi.isdigit():
                messagebox.showerror("Error", "กรุณากรอกรหัสไปรษณีย์ให้ถูกต้อง")
            elif len(pi) != 5 :
                messagebox.showerror("Error", "รหัสไปรษณีย์ต้องมี 5 หลัก")

            else:
                cursor.execute(
                    "INSERT INTO register (username, password, name, IDcard, phone, home_number, m, s, r, d, dis, pro, pi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (username, password, name, idcard, phone, home_number, m, s, r, d, dis, pro, pi),
                )
                
                conn.commit()
                messagebox.showinfo("Success", "Registration successful!")
                
                
                login()

            


    
    img = Image.open("E:\PythonPJ\PythonPJ\BG1Reg.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow, image=photo)
    lbl.pack()
    lbl.image = photo

    

    registerEntry=Entry(currentwindow,width=30,font=25,bd=0)
    registerEntry.place(x=465,y=322)

    passwordEntry=Entry(currentwindow,width=25,font=25,bd=0)
    passwordEntry.place(x=482,y=382)

    idcardEntry=Entry(currentwindow,width=18,font=25,bd=0)
    idcardEntry.place(x=587,y=418)

    nameEntry=Entry(currentwindow,width=25,font=25,bd=0)
    nameEntry.place(x=470,y=456)

    telEntry=Entry(currentwindow,width=25,font=25,bd=0)
    telEntry.place(x=500,y=490)

    homenbEntry=Entry(currentwindow,width=6,font=25,bd=0)
    homenbEntry.place(x=458,y=565)

    mEntry=Entry(currentwindow,width=7,font=25,bd=0)
    mEntry.place(x=580,y=565)

    sEntry=Entry(currentwindow,width=7,font=25,bd=0)
    sEntry.place(x=715,y=565)

    rEntry=Entry(currentwindow,width=7,font=25,bd=0)
    rEntry.place(x=420,y=602)

    dEntry=Entry(currentwindow,width=11,font=25,bd=0)
    dEntry.place(x=578,y=606)

    disEntry=Entry(currentwindow,width=9,font=25,bd=0)
    disEntry.place(x=437,y=645)

    proEntry=Entry(currentwindow,width=9,font=25,bd=0)
    proEntry.place(x=640,y=645)

    piEntry=Entry(currentwindow,width=9,font=25,bd=0)
    piEntry.place(x=505,y=682)

#ยืนยันการสมัคร
    btsubreg = Button(currentwindow)
    btsubreg.place(relx=0.588, rely=0.855 ,width=122, height=19) 
    btsubreg.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/BGReg/buttonregCF.png")
    btsubreg.configure(image=img5)
    btsubreg.configure(command=regis)
    btsubreg.image = img5 

#เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

#วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
    btbooking.configure(command=howto)
    btbooking.image = img3

#ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    btcantact.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

    
def fetch_data1():
    conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, date, status1 FROM STD1")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data2():
    conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, date, status2 FROM STD2")
    data = cursor.fetchall()
    conn.close()
    return data


def fetch_data3():
    conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, date, status3 FROM STD3")
    data = cursor.fetchall()
    conn.close()
    return data


def login():
    global currentwindow
    if currentwindow:
        currentwindow.destroy ()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')
    img = Image.open("E:\PythonPJ\PythonPJ\BGLogin.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow, image=photo)
    lbl.pack()
    lbl.image = photo
    logged_in_name=''

    
#เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

  

#วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
    btbooking.configure(command=howto)
    btbooking.image = img3

#ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015, width=175, height=52)
    btcantact.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

    

       
    
    def authenticate():
        nonlocal logged_in_name
        username = registerEntry.get()
        password = passwordEntry.get()
    
        conn = sqlite3.connect("E:/PythonPJ/PythonPJ/khantepStudio1_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM register WHERE username=? AND password=?", (username, password))
        log = c.fetchone()
        
        
        if log:
            logged_in_name = log[3]  # Store the logged-in user's name
            messagebox.showinfo("Login Successful", "Welcome, " + logged_in_name)
            homepage2()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            login()
            
        
        


    registerEntry = Entry( currentwindow,width=25,font=25,bd=0)
    registerEntry.place(x=520,y=425)

    passwordEntry = Entry( currentwindow, width=25,font=25,bd=0,show='*')
    passwordEntry.place(x=520,y=480)

            

        


    #ยืนยันเข้าสู่ระบบ
    btlogincon = Button(currentwindow)
    btlogincon.place(relx=0.613, rely=0.597 ,width=80, height=19) 
    btlogincon.configure(relief="flat",overrelief="flat",activebackground="#0c00a5",cursor="hand2",foreground="#0c00a5",background="#0c00a5",borderwidth='0')
    img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
    btlogincon.configure(image=img5)
    btlogincon.configure(command=authenticate)
    btlogincon.image = img5
    
    def contactforuser():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        img = Image.open("BGติดต่อ.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo       # เก็บ reference รูป

        #เช็คตารางห้อง
        Btcheck = Button(currentwindow)
        Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
        Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
        Btcheck.configure(image=img2)
        Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
        Btcheck.image = img2

    #วิธีการจองห้อง
        btbooking = Button(currentwindow)
        btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
        btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        btbooking.configure(image=img3)
        btbooking.configure(command=howto)
        btbooking.image = img3

    #ติดต่อ
        btcantact = Button(currentwindow)
        btcantact.place(relx=0.42, rely=0.015 ,width=175, height=52) 
        btcantact.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
        btcantact.configure(image=img4)
        btcantact.configure(command=contactforuser)
        btcantact.image = img4

    #LOGOKHANTEP
        btlogo = Button(currentwindow)
        btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
        btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        btlogo.configure(image=img7)
        btlogo.configure(command=homepage2)
        btlogo.image = img7


    def forcheck():
        global currentwindow
        if currentwindow:
            currentwindow.destroy ()
        
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        img = Image.open("E:\PythonPJ\PythonPJ\BGเช็คตาราง.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo       # เก็บ reference รูป

        data = fetch_data1()
        x_default = 160
        y_default = 422
        for name, date, status in data:
            if status == "Paid":
                masked_name = name[:2] + '*' * 3 + name[-3:]  # Replace the actual name with five asterisks
                Label(currentwindow, background="#c64646", fg="white", activebackground="#000000", borderwidth='0', font=("Helvetica", 9), text=f" วันที่ :  {date}  ผู้จอง :  {masked_name}").place(x=x_default, y=y_default)

                y_default += 35

        data = fetch_data2()
        x_default = 470
        y_default = 422
        for name, date, status in data:
            if status == "Paid":
                masked_name = name[:2] + '*' * 3 + name[-3:]  # Replace the actual name with five asterisks
                Label(currentwindow, background="#c64646", fg="white", activebackground="#000000", borderwidth='0', font=("Helvetica", 9), text=f" วันที่ :  {date}  ผู้จอง :  {masked_name}").place(x=x_default, y=y_default)

                y_default += 35

        data = fetch_data3()
        x_default = 780
        y_default = 422
        for name, date, status in data:
            if status == "Paid":
                masked_name = name[:2] + '*' * 3 + name[-3:]  # Replace the actual name with five asterisks
                Label(currentwindow, background="#c64646", fg="white", activebackground="#000000", borderwidth='0', font=("Helvetica", 9), text=f" วันที่ :  {date}  ผู้จอง :  {masked_name}").place(x=x_default, y=y_default)

                y_default += 35


    #เช็คตารางห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
        Button1.configure(image=img2)
        Button1.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
        Button1.image = img2

    #วิธีการจองห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        Button1.configure(image=img3)
        Button1.configure(command=currentwindow)
        Button1.image = img3

    #ติดต่อ
        Button1 = Button(currentwindow)
        Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
        Button1.configure(image=img4)
        # Button1.configure(command=contact)
        Button1.image = img4
        
    #LOGOKHANTEP
        Button1 = Button(currentwindow)
        Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        Button1.configure(image=img7)
        Button1.configure(command=homepage2)
        Button.image = img7

        

    def homepage2():
        
        # nonlocal logged_in_name
        global currentwindow
        if currentwindow:
            currentwindow.destroy ()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        img = Image.open("BG3AfterLogin.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo       # เก็บ reference รูป

        name_label = Label(currentwindow, text=f' {logged_in_name}',bg='white' ,bd=0,font=30)
        name_label.place(x=570,y=734)


    #เลือกจองห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เลือกจองห้อง.png")
        Button1.configure(image=img2)
        Button1.configure(command=Bookingstu1)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
        Button1.image = img2

    #เช็คตารางห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
        Button1.configure(image=img3)
        Button1.configure(command=forcheck)
        Button1.image = img3

    #ออกจากระบบ
        Button1 = Button(currentwindow)
        Button1.place(x=1050,y=80) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#646162",borderwidth='0')
        img3 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\BTออกจากระบบ.png")
        Button1.configure(image=img3)
        Button1.configure(command=HomePage)
        Button1.image = img3


    #วิธีการจอง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.48, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        Button1.configure(image=img4)
        Button1.configure(command=howto)
        Button1.image = img4

    #ติดต่อ
        Button1 = Button(currentwindow)
        Button1.place(relx=0.65, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
        Button1.configure(image=img5)
        Button1.configure(command=contactforuser)
        Button1.image = img5

    #LOGOKHANTEP
        Button1 = Button(currentwindow)
        Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        Button1.configure(image=img7)
        Button1.configure(command=homepage2)
        Button.image = img7

    def Bookingstu1():
        nonlocal logged_in_name
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
         
        
         
        def windowconfirm1():
                
                global currentwindow,windowpopup1
                dmy = StringVar()
                endmy = Entry(textvariable=dmy)  
           
               
            # Setting หน้าจอโปรแกรม


                windowpopup1 = Toplevel(currentwindow)
                windowpopup1.title("KHANTEP STUDIO")
                windowpopup1.geometry("520x520+750+300")
                windowpopup1.iconbitmap('KhantepStudio.ico')
                
                
                
                

                #Nameuser,Phonenumber
                name_user = str()
                phone = str()
                idcard = str()
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if str(x[3]) == str(logged_in_name):
                        name_user = str(x[3])
                        phone = str(x[5])    
                        idcard= str(x[4])
                


                

            #BG ทั้งหมด
                img = Image.open("E:\PythonPJ\PythonPJ\WindowใบจองSelf-ServiceStudio.png")       
                photo = ImageTk.PhotoImage(img)
                lbl = Label(windowpopup1, image=photo)
                lbl.pack()
                lbl.image = photo
            #Exit
                Button1 = Button(windowpopup1)
                Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
                img5 = PhotoImage(file=r"ButtonExit.png")
                Button1.configure(command=HomePage)
                Button1.configure(image=img5)
                Button1.image = img5    
                
                name_userShow   = Label(windowpopup1, text=f' {name_user}',bg='white',font=25,bd=0 )
                name_userShow.place(x=125,y=127)
                phoneNumber_label = Label(windowpopup1, text=f' {phone}', bg='white',font=25,bd=0)
                phoneNumber_label.place(x=155, y=170)
                idcardshow= Label(windowpopup1, text=f' {idcard}',bg='white',font=25,bd=0 )
                current_time = datetime.now().strftime('%H:%M:%S')
                time_label = Label(windowpopup1, text=f': {current_time}', bg='white', font=25, bd=0)
                

                

                # สร้างตัวแปรสำหรับรายการใน combobox
                items = ["Self-ServiceStudio"]

                # สร้าง combobox
                combo = ttk.Combobox(windowpopup1, values=items,width=20,font=20,state="readonly")
                combo.place(x=130,y=213)
                combo.current(0)
                
                # ฟังก์ชันสำหรับการเลือกรายการใน combobox
                def on_select(event):
                    selected_item = combo.get()

                combo.bind("<<ComboboxSelected>>", on_select)

                    

                def pick_date(event):
                    global currentwindow, windowpopup1
                    date_window = Toplevel()
                    date_window.grab_set()
                    date_window.title("DATE")
                    date_window.geometry("250x220+350+320")
                    current_date=datetime.now().strftime("%d-%m-%Y")
                    cal = Calendar(date_window, selectmode="day", date_pattern="dd-mm-yyyy")
                    cal.place(x=0, y=0)

                    def grab_date():
                        selected_date = cal.get_date()
                        
                        # Check if the selected date already exists in the database
                        cursor.execute("SELECT * FROM STD1 WHERE date=?", (selected_date,))
                        existing_record = cursor.fetchone()


                        if existing_record:
                            messagebox.showerror("เกิดข้อผิดพลาด", "วันที่นี้มีการจองแล้ว")
                        
                        elif selected_date < current_date:
                            messagebox.showerror("เกิดข้อผิดพลาด", "กรุณาจองให้ถูกต้อง")

                        else:
                            endmy.delete(0, END)
                            endmy.insert(0, selected_date)
                            endmy.config(fg="red")
                            date_window.destroy()
                            
                            

                    submit_btn = Button(date_window, text='Submit', command=grab_date, width=20, cursor="hand2")
                    submit_btn.place(x=80, y=190)

                endmy = Entry(windowpopup1, textvariable=dmy, width=33, borderwidth=0)
                endmy.place(x=110, y=258)
                endmy.config(font=15)
                endmy.bind("<1>",pick_date)

                
                def confirmstd1():
                
                    usernamestd1 = name_userShow.cget("text")
                    idcardstd1=idcardshow.cget("text")
                    phonestd1 = phoneNumber_label.cget("text")
                    selected_itemstd1 = combo.get()
                    endmystd1 = endmy.get()
                    current_time_str = current_time  # ใช้ตัวแปร current_time ที่ได้สร้างไว้ก่อนหน้านี้
                    day,month,year=map(int,endmystd1.split("-"))
                    

                    insert_query1 = "INSERT INTO STD1 (name, studio, date,time,day,month,year) VALUES (?, ?, ?,?,?, ?, ?)"
                    cursor.execute(insert_query1, (usernamestd1, selected_itemstd1,endmystd1,current_time_str,day,month,year))
                    insert_query2 = "INSERT INTO history (name,IDcard,phone,studio,date,time) VALUES (?,?,?,?,?,?)"
                    cursor.execute(insert_query2, (usernamestd1,idcardstd1,phonestd1, selected_itemstd1,endmystd1,current_time_str))
                    conn.commit()
                    messagebox.showinfo("จองสำเร็จ", "กรุณาชำระตามยอดเงินและรอสถานะอัพเดท")


                #ยืนยันการจอง
                Button1 = Button(windowpopup1)
                Button1.place(relx=0.77, rely=0.64 ,width=80, height=19) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
                img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ButtonConfirm.png")
                Button1.configure(image=img5)
                Button1.configure(command=confirmstd1)
                Button1.image = img5 



              
                
        # Setting หน้าจอโปรแกรม
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')
        #BG ทั้งหมด
        img = Image.open(r"E:\PythonPJ\PythonPJ\BGSelf-ServiceStudio1.png")       
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo

        
        #LOGOKHANTEP
        Button1 = Button(currentwindow)
        Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        Button1.configure(image=img1)
        Button1.configure(command=homepage2)
        Button1.image = img1    

        #เช็คตารางห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
        Button1.configure(image=img2)
        Button1.configure(command=forcheck)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
        Button1.image = img2

        #วิธีการจองห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        Button1.configure(image=img3)
        Button1.configure(command=HomePage)
        Button1.image = img3

        #ติดต่อ
        Button1 = Button(currentwindow)
        Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
        Button1.configure(image=img4)
        # Button1.configure(command=contact)
        Button1.image = img4

        #กดเพื่อจอง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.69, rely=0.315 ,width=80, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
        img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonจองเลย.png")
        Button1.configure(image=img5)
        Button1.configure(command=windowconfirm1)
        Button1.image = img5

        #กดเพื่อไปหน้าถัดไป 
        Button1 = Button(currentwindow)
        Button1.place(relx=0.876, rely=0.82 ,width=30, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonหน้าถัดไป.png")
        Button1.configure(image=img6)
        Button1.configure(command=Bookingstu2) 
        Button1.image = img6 

        

    def Bookingstu2():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        
        def windowconfirm2():
                
                global currentwindow,windowpopup2
                dmy = StringVar()
                endmy = Entry(textvariable=dmy)  
           
               
            # Setting หน้าจอโปรแกรม


                windowpopup2 = Toplevel(currentwindow)
                windowpopup2.title("KHANTEP STUDIO")
                windowpopup2.geometry("520x520+750+300")
                windowpopup2.iconbitmap('KhantepStudio.ico')
                
                #BG ทั้งหมด
                img = PhotoImage(file="E:\PythonPJ\PythonPJ\Windowใบจอง MiniStudio.png")
                lbl = Label(windowpopup2, image=img)
                lbl.image = img  
                lbl.pack()
                
                

                #Nameuser,Phonenumber
                name_user = str()
                phone = str()
                idcard = str()
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if str(x[3]) == str(logged_in_name):
                        name_user = str(x[3])
                        phone = str(x[5])    
                        idcard= str(x[4])
                
                

                

            
            #Exit
                Button1 = Button(windowpopup2)
                Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
                img5 = PhotoImage(file=r"ButtonExit.png")
                Button1.configure(command=HomePage)
                Button1.configure(image=img5)
                Button1.image = img5    
                name_userShow   = Label(windowpopup2, text=f' {name_user}',bg='white',font=25,bd=0 )
                name_userShow.place(x=125,y=127)
                phoneNumber_label = Label(windowpopup2, text=f' {phone}', bg='white',font=25,bd=0)
                phoneNumber_label.place(x=155, y=170)
                idcardshow= Label(windowpopup2, text=f' {idcard}',bg='white',font=25,bd=0 )
                current_time = datetime.now().strftime('%H:%M:%S')
                time_label = Label(windowpopup2, text=f': {current_time}', bg='white', font=25, bd=0)
                
               

                

                # สร้างตัวแปรสำหรับรายการใน combobox
                items = ["BGMiniStudio"]

                # สร้าง combobox
                combo = ttk.Combobox(windowpopup2, values=items,width=20,font=20,state="readonly")
                combo.place(x=130,y=213)
                combo.current(0)
                # ฟังก์ชันสำหรับการเลือกรายการใน combobox
                def on_select(event):
                    selected_item = combo.get()

                combo.bind("<<ComboboxSelected>>", on_select)

                    

                def pick_date(event):
                    global currentwindow, windowpopup2
                    date_window = Toplevel()
                    date_window.grab_set()
                    date_window.title("DATE")
                    date_window.geometry("250x220+350+320")
                    current_date=datetime.now().strftime("%d-%m-%Y")
                    cal = Calendar(date_window, selectmode="day", date_pattern="dd-mm-yyyy")
                    cal.place(x=0, y=0)

                    def grab_date():
                        selected_date = cal.get_date()
                        
                        # Check if the selected date already exists in the database
                        cursor.execute("SELECT * FROM STD2 WHERE date=?", (selected_date,))
                        existing_record = cursor.fetchone()

                        if existing_record:
                            messagebox.showerror("เกิดข้อผิดพลาด", "วันที่นี้มีการจองแล้ว")
                        
                        elif selected_date < current_date:
                            messagebox.showerror("เกิดข้อผิดพลาด", "กรุณาจองให้ถูกต้อง")

                        else:
                            endmy.delete(0, END)
                            endmy.insert(0, selected_date)
                            endmy.config(fg="red")
                            date_window.destroy()

                    submit_btn = Button(date_window, text='Submit', command=grab_date, width=20, cursor="hand2")
                    submit_btn.place(x=80, y=190)

                endmy = Entry(windowpopup2, textvariable=dmy, width=33, borderwidth=0)
                endmy.place(x=110, y=258)
                endmy.config(font=15)
                endmy.bind("<1>",pick_date)

                def confirmstd2():
                
                    usernamestd2 = name_userShow.cget("text")
                    idcardstd2=idcardshow.cget("text")
                    phonestd2 = phoneNumber_label.cget("text")
                    selected_itemstd2 = combo.get()
                    endmystd2 = endmy.get()
                    current_time_str = current_time  # ใช้ตัวแปร current_time ที่ได้สร้างไว้ก่อนหน้านี้
                    day,month,year=map(int,endmystd2.split("-"))


                    insert_query1 = "INSERT INTO STD2 (name, studio, date,time,day,month,year) VALUES (?, ?, ?,?,?, ?, ?)"
                    cursor.execute(insert_query1, (usernamestd2, selected_itemstd2,endmystd2,current_time_str,day,month,year))
                    insert_query2 = "INSERT INTO history (name,IDcard,phone,studio,date,time) VALUES (?,?,?,?,?,?)"
                    cursor.execute(insert_query2, (usernamestd2,idcardstd2,phonestd2, selected_itemstd2,endmystd2,current_time_str))
                    conn.commit()
                    messagebox.showinfo("จองสำเร็จ", "กรุณาชำระตามยอดเงินและรอสถานะอัพเดท")


                #ยืนยันการจอง
                Button1 = Button(windowpopup2)
                Button1.place(relx=0.77, rely=0.64 ,width=80, height=19)  
                Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
                img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ButtonConfirm.png")
                Button1.configure(image=img5)
                Button1.configure(command=confirmstd2)
                Button1.image = img5 
                


        # Setting หน้าจอโปรแกรม
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        #BG ทั้งหมด
        img = Image.open("BGMiniStudio.png")       
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo

    #LOGOKHANTEP
        Button1 = Button(currentwindow)
        Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        Button1.configure(image=img1)
        Button1.configure(command=homepage2)
        Button1.image = img1

    #เช็คตารางห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
        Button1.configure(image=img2)
        Button1.configure(command=forcheck)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
        Button1.image = img2

    #วิธีการจองห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        Button1.configure(image=img3)
        Button1.configure(command=HomePage)
        Button1.image = img3

    #ติดต่อ
        Button1 = Button(currentwindow)
        Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
        Button1.configure(image=img4)
        # Button1.configure(command=contact)
        Button1.image = img4

    #กดเพื่อจอง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.61, rely=0.315 ,width=80, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
        img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonจองเลย.png")
        Button1.configure(image=img5)
        Button1.configure(command=windowconfirm2)
        Button1.image = img5

    #กดเพื่อไปหน้าถัดไป 
        Button1 = Button(currentwindow)
        Button1.place(relx=0.876, rely=0.82 ,width=30, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonหน้าถัดไป.png")
        Button1.configure(image=img6)
        Button1.configure(command=Bookingstu3)
        Button1.image = img6

    #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(relx=0.159, rely=0.82 ,width=30, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=Bookingstu1)
        Button1.image = img7  
    
    def Bookingstu3():
        global currentwindow
        currentwindow.destroy()
       
        def windowconfirm3():
                
                global currentwindow,windowpopup3
                dmy = StringVar()
                endmy = Entry(textvariable=dmy)  
           
               
            # Setting หน้าจอโปรแกรม


                windowpopup3 = Toplevel(currentwindow)
                windowpopup3.title("KHANTEP STUDIO")
                windowpopup3.geometry("520x520+750+300")
                windowpopup3.iconbitmap('KhantepStudio.ico')
                
                
                
                

                #Nameuser,Phonenumber
                name_user = str()
                phone = str()
                idcard = str()
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if str(x[3]) == str(logged_in_name):
                        name_user = str(x[3])
                        phone = str(x[5])    
                        idcard= str(x[4])    
                
                

                

            #BG ทั้งหมด
                img = PhotoImage(file="E:\PythonPJ\PythonPJ\Windowใบจอง MainStudio.png")
                lbl = Label(windowpopup3, image=img)
                lbl.image = img  
                lbl.pack()
            #Exit
                Button1 = Button(windowpopup3)
                Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
                img5 = PhotoImage(file=r"ButtonExit.png")
                Button1.configure(command=HomePage)
                Button1.configure(image=img5)
                Button1.image = img5    
                name_userShow   = Label(windowpopup3, text=f' {name_user}',bg='white',font=25,bd=0 )
                name_userShow.place(x=125,y=127)
                phoneNumber_label = Label(windowpopup3, text=f' {phone}', bg='white',font=25,bd=0)
                phoneNumber_label.place(x=155, y=170)
                idcardshow= Label(windowpopup3, text=f' {idcard}',bg='white',font=25,bd=0 )
                current_time = datetime.now().strftime('%H:%M:%S')
                time_label = Label(windowpopup3, text=f': {current_time}', bg='white', font=25, bd=0)

                

                # สร้างตัวแปรสำหรับรายการใน combobox
                items = ["BGMainStudio"]

                # สร้าง combobox
                combo = ttk.Combobox(windowpopup3, values=items,width=20,font=20,state="readonly")
                combo.place(x=130,y=213)
                combo.current(0)
                # ฟังก์ชันสำหรับการเลือกรายการใน combobox
                def on_select(event):
                    selected_item = combo.get()

                combo.bind("<<ComboboxSelected>>", on_select)

                    

                def pick_date(event):
                    global currentwindow, windowpopup3
                    date_window = Toplevel()
                    date_window.grab_set()
                    date_window.title("DATE")
                    date_window.geometry("250x220+350+320")
                    current_date=datetime.now().strftime("%d-%m-%Y")
                    cal = Calendar(date_window, selectmode="day", date_pattern="dd-mm-yyyy")
                    cal.place(x=0, y=0)


                    def grab_date():
                        selected_date = cal.get_date()
                        
                        # Check if the selected date already exists in the database
                        cursor.execute("SELECT * FROM STD3 WHERE date=?", (selected_date,))
                        existing_record = cursor.fetchone()

                        if existing_record:
                            messagebox.showerror("เกิดข้อผิดพลาด", "วันที่นี้มีการจองแล้ว")
                        
                        elif selected_date < current_date:
                            messagebox.showerror("เกิดข้อผิดพลาด", "กรุณาจองให้ถูกต้อง")
                            
                        else:
                            endmy.delete(0, END)
                            endmy.insert(0, selected_date)
                            endmy.config(fg="red")
                            date_window.destroy()

                    submit_btn = Button(date_window, text='Submit', command=grab_date, width=20, cursor="hand2")
                    submit_btn.place(x=80, y=190)

                endmy = Entry(windowpopup3, textvariable=dmy, width=33, borderwidth=0)
                endmy.place(x=110, y=258)
                endmy.config(font=15)
                endmy.bind("<1>",pick_date)
                


                def confirmstd3():
                    
                    usernamestd3 = name_userShow.cget("text")
                    idcardstd3=idcardshow.cget("text")
                    phonestd3 = phoneNumber_label.cget("text")
                    selected_itemstd3 = combo.get()
                    endmystd3 = endmy.get()
                    current_time_str = current_time  # ใช้ตัวแปร current_time ที่ได้สร้างไว้ก่อนหน้านี้
                    day,month,year=map(int,endmystd3.split("-"))


                    insert_query1 = "INSERT INTO STD3 (name, studio, date,time,day,month,year) VALUES (?, ?, ?,?,?, ?, ?)"
                    cursor.execute(insert_query1, (usernamestd3, selected_itemstd3,endmystd3,current_time_str,day,month,year))
                    insert_query2 = "INSERT INTO history (name,IDcard,phone,studio,date,time) VALUES (?,?,?,?,?,?)"
                    cursor.execute(insert_query2, (usernamestd3,idcardstd3,phonestd3, selected_itemstd3,endmystd3,current_time_str))
                    conn.commit()
                    messagebox.showinfo("จองสำเร็จ", "กรุณาชำระตามยอดเงินและรอสถานะอัพเดท")

                
                #ยืนยันการจอง
                Button1 = Button(windowpopup3)
                Button1.place(relx=0.77, rely=0.64 ,width=80, height=19)  
                Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
                img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/buttonregยืนยันการจอง.png")
                Button1.configure(image=img5)
                Button1.configure(command=confirmstd3)
                Button1.image = img5 
                


        # Setting หน้าจอโปรแกรม
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        #BG ทั้งหมด
        img = Image.open("BGMainStudio.png")       
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo

    #LOGOKHANTEP
        Button1 = Button(currentwindow)
        Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        Button1.configure(image=img1)
        Button1.configure(command=homepage2)
        Button1.image = img1

    #เช็คตารางห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
        Button1.configure(image=img2)
        Button1.configure(command=forcheck)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
        Button1.image = img2

    #วิธีการจองห้อง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        Button1.configure(image=img3)
        Button1.configure(command=HomePage)
        Button1.image = img3

    #ติดต่อ
        Button1 = Button(currentwindow)
        Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
        Button1.configure(image=img4)
        Button1.configure(command=contactforuser)
        Button1.image = img4

    #กดเพื่อจอง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.61, rely=0.315 ,width=80, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
        img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonจองเลย.png")
        Button1.configure(image=img5)
        Button1.configure(command=windowconfirm3)
        Button1.image = img5

       #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(relx=0.159, rely=0.82 ,width=30, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=Bookingstu2)
        Button1.image = img7  
    
def loginforadmin():
    global currentwindow
    if currentwindow:
        currentwindow.destroy ()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')
    img = Image.open("E:\PythonPJ\PythonPJ\BGReg\BGLoginadmin.jpg")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow, image=photo)
    lbl.pack()
    lbl.image = photo
    

    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        # สร้างปุ่มเข้าสู่ระบบ
        login_button = Button(currentwindow, text="เข้าสู่ระบบ", command=check_login)
        login_button.pack()
    
        if username == "admin" and password == "a":  # ตรวจสอบ username และ password ที่ถูกต้อง
            messagebox.showinfo("Login Successful", "เข้าสู่ระบบสำเร็จ")
            foradmin()
            # เพิ่มโค้ดเปิดหน้าหลักหลังจากเข้าสู่ระบบสำเร็จ
        else:
            messagebox.showerror("Login Failed", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

    username_entry = Entry( currentwindow,width=25,font=25,bd=0)
    username_entry.place(x=520,y=425)

    password_entry = Entry( currentwindow, width=25,font=25,bd=0,show='*')
    password_entry.place(x=520,y=480)


    
#เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

    

#วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
    # btbooking.configure(command=homepage2)
    btbooking.image = img3

#ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015, width=175, height=52)
    btcantact.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

    #ยืนยันเข้าสู่ระบบ
    btlogincon = Button(currentwindow)
    btlogincon.place(relx=0.613, rely=0.597 ,width=80, height=19) 
    btlogincon.configure(relief="flat",overrelief="flat",activebackground="#0c00a5",cursor="hand2",foreground="#0c00a5",background="#0c00a5",borderwidth='0')
    img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
    btlogincon.configure(image=img5)
    btlogincon.configure(command=check_login)
    btlogincon.image = img5

def HomePage():
    
    global currentwindow
    if currentwindow:
        currentwindow.destroy ()
    #Homepage
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')
    img = Image.open(r"E:\PythonPJ\PythonPJ\BG2.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow,image=photo)
    lbl.pack()
    lbl.image = photo

    
    #rge
    bthomepage = Button(currentwindow)
    bthomepage.place(relx=0.543, rely=0.832 ,width=143, height=33) 
    bthomepage.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img6 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button reg.png")
    bthomepage.configure(image=img6)
    bthomepage.configure(command=registerPage)
    bthomepage.image = img6

    #login
    btlogin = Button(currentwindow)
    btlogin.place(relx=0.388, rely=0.832 ,width=105, height=33) 
    btlogin.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button login12.png")
    btlogin.configure(image=img5)
    btlogin.configure(command=login)
    btlogin.image = img5 
   
    #admin
    btlogincon = Button(currentwindow)
    btlogincon.place(relx=0.700, rely=0.015 ,width=175, height=52) 
    btlogincon.configure(relief="flat",overrelief="flat",activebackground="#0c00a5",cursor="hand2",foreground="#0c00a5",background="#0c00a5",borderwidth='0')
    img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\admin.png")
    btlogincon.configure(image=img6)
    btlogincon.configure(command=loginforadmin)
    btlogincon.image = img6

    #เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

    #วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
    btbooking.configure(command=howto)
    btbooking.image = img3

    #ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    btcantact.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

    #LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7



def howto():
    global currentwindow
    if currentwindow:
        currentwindow.destroy ()
    #Homepage
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')
    img = Image.open(r"E:\PythonPJ\PythonPJ\วิธีการจองห้อง.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow,image=photo)
    lbl.pack()
    lbl.image = photo

    #เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

  

#วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
    btbooking.configure(command=howto)
    btbooking.image = img3

#ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015, width=175, height=52)
    btcantact.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

def check():
    global currentwindow
    if currentwindow:
        currentwindow.destroy ()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')


    img = Image.open(r"E:\PythonPJ\PythonPJ\BGเช็คตาราง.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow,image=photo)
    lbl.pack()
    lbl.image = photo

    data = fetch_data1()
    x_default = 160
    y_default = 422
    for name, date, status in data:
        if status == "Paid":
            masked_name = name[:2] + '*' * 3 + name[-3:]  # Replace the actual name with five asterisks
            Label(currentwindow, background="#c64646", fg="white", activebackground="#000000", borderwidth='0', font=("Helvetica", 9), text=f" วันที่ :  {date}  ผู้จอง :  {masked_name}").place(x=x_default, y=y_default)

            y_default += 35

    data = fetch_data2()
    x_default = 470
    y_default = 422
    for name, date, status in data:
        if status == "Paid":
            masked_name = name[:2] + '*' * 3 + name[-3:]  # Replace the actual name with five asterisks
            Label(currentwindow, background="#c64646", fg="white", activebackground="#000000", borderwidth='0', font=("Helvetica", 9), text=f" วันที่ :  {date}  ผู้จอง :  {masked_name}").place(x=x_default, y=y_default)

            y_default += 35

    data = fetch_data3()
    x_default = 780
    y_default = 422
    for name, date, status in data:
        if status == "Paid":
            masked_name = name[:2] + '*' * 3 + name[-3:]  # Replace the actual name with five asterisks
            Label(currentwindow, background="#c64646", fg="white", activebackground="#000000", borderwidth='0', font=("Helvetica", 9), text=f" วันที่ :  {date}  ผู้จอง :  {masked_name}").place(x=x_default, y=y_default)

            y_default += 35


    #เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

#วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
#     btbooking.configure(command=homePage)
    btbooking.image = img3

#ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    btcantact.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

def contact():
    global currentwindow
    if currentwindow:
        currentwindow.destroy()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')

    img = Image.open(r"E:\PythonPJ\PythonPJ\BGติดต่อ.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow,image=photo)
    lbl.pack()
    lbl.image = photo

    #เช็คตารางห้อง
    Btcheck = Button(currentwindow)
    Btcheck.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Btcheck.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Btcheck.configure(image=img2)
    Btcheck.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Btcheck.image = img2

#วิธีการจองห้อง
    btbooking = Button(currentwindow)
    btbooking.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    btbooking.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
    btbooking.configure(image=img3)
    btbooking.configure(command=howto)
    btbooking.image = img3

#ติดต่อ
    btcantact = Button(currentwindow)
    btcantact.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    btcantact.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    btcantact.configure(image=img4)
    btcantact.configure(command=contact)
    btcantact.image = img4

#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

def foradmin():
    global currentwindow
    if currentwindow:
        currentwindow.destroy()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')
    

    
    
    img = Image.open(r"E:\PythonPJ\PythonPJ\BGAdmin.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow,image=photo)
    lbl.pack()
    lbl.image = photo

    
#LOGOKHANTEP
    btlogo = Button(currentwindow)
    btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    btlogo.configure(image=img7)
    btlogo.configure(command=HomePage)
    btlogo.image = img7

    


    usn=''
    pw=''
    n=''
    idc=''
    tel=''
    hn=''
    m=''
    s=''
    r=''
    d=''
    dis=''
    pro=''
    pi=''




    def history():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\historyStudio.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)
        

        def show_history():
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM history")
            data = cursor.fetchall()

            conn.close()

            for item in tree.get_children():
                tree.delete(item)

            for row in data:
                tree.insert("", "end", values=row)

        # Create Treeview widget
        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "ID Card", "Phone", "Studio", "Date", "Time"))
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="ID Card")
        tree.heading("#4", text="Phone")
        tree.heading("#5", text="Studio")
        tree.heading("#6", text="Date")
        tree.heading("#7", text="Time")

        # Set the column widths
        tree.column("#1", anchor="center", width=50)
        tree.column("#2", anchor="center", width=150)
        tree.column("#3", anchor="center", width=150)
        tree.column("#4", anchor="center", width=100)
        tree.column("#5", anchor="center", width=150)
        tree.column("#6", anchor="center", width=100)
        tree.column("#7", anchor="center", width=100)
        tree.column("#0", anchor="center", width=0, stretch='NO')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)   
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)


        


        show_history()
       
        def delete_selected():
    # Get the selected item(s) in the Treeview widget
            selected_items = tree.selection()

            if not selected_items:
                messagebox.showwarning("No Selection", "Please select a row to delete.")
                return

            # Prompt the user for confirmation
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?")

            if not confirm:
                return  # User chose not to delete

            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")  # เปลี่ยนเป็นชื่อฐานข้อมูลของคุณ
            cursor = conn.cursor()

            for item in selected_items:
                # Get the ID (assuming it's in the first column)
                id_to_delete = tree.item(item, "values")[0]

                # Delete the item from the Treeview
                tree.delete(item)

                # Delete the corresponding record from the database
                cursor.execute("DELETE FROM history WHERE ID=?", (id_to_delete,))
                conn.commit()
       
       
       
        def delete_all():
    # Prompt the user for confirmation
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all rows?")
            
            if not confirm:
                return  # User chose not to delete

            # Clear all items in the Treeview widget
            for item in tree.get_children():
                tree.delete(item)

            # Delete all records from the database
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")  # เปลี่ยนเป็นชื่อฐานข้อมูลของคุณ
            cursor = conn.cursor()

            cursor.execute("DELETE FROM history")
            conn.commit()

        # Create a button to refresh the data
        btcnedit = Button(currentwindow)
        btcnedit.place(x=350,y=590) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\แสดงข้อมูลใหม่.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=show_history)
        btcnedit.image = img8

        btcnedit = Button(currentwindow)
        btcnedit.place(x=500,y=590) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ลบแถวที่เลือก.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=delete_selected)
        btcnedit.image = img8

        btcnedit = Button(currentwindow)
        btcnedit.place(x=650,y=590) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ลบทั้งหมด.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=delete_all)
        btcnedit.image = img8

        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=foradmin)
        Button1.image = img7


    def std1():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')
        
        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\UpdateSTD1.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)


        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=foradmin)
        Button1.image = img7

        def showstd1():
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM STD1")
            data = cursor.fetchall()
            for row in data:
                tree.insert("", "end", values=row)

        # Create Treeview
        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date", "Time", "Status"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")
        tree.heading("Status", text="Status")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)
        tree.column("Time", anchor="center", width=100)
        tree.column("Status", anchor="center", width=100)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)   
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)
        

        def update_status():
            selected_item = tree.selection()[0]
            new_status = status_combo.get()
            tree.item(selected_item, values=(tree.item(selected_item)['values'][0], tree.item(selected_item)['values'][1], tree.item(selected_item)['values'][2], tree.item(selected_item)['values'][3], tree.item(selected_item)['values'][4], new_status))


            # Update the database with the new status
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE STD1 SET status1 = ? WHERE id = ?", (new_status, tree.item(selected_item)['values'][0]))
            conn.commit()
            conn.close()


        # Create Combobox for Status
        status_combo = ttk.Combobox(currentwindow, values=["Paid", "Not Paid"],state="readonly")
        status_combo.place(x=435, y=635)



        btcnedit = Button(currentwindow)
        btcnedit.place(x=612, y=635 ,width=110, height=31) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonregยืนยันข้อมูล2.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=update_status)
        btcnedit.image = img8

        def delete_selected():
            # Get the selected item(s) in the Treeview widget
            selected_items = tree.selection()

            if not selected_items:
                messagebox.showwarning("No Selection", "กรุณาเลือกแถวที่ต้องการยกเลิกการจอง")
                return

            # Prompt the user for confirmation
            confirm = messagebox.askyesno("แจ้งเตือน", "คุณต้องการยกเลิกการจองนี้หรือไม่")

            if not confirm:
                return  # User chose not to delete

            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()

            for item in selected_items:
                # Get the ID (assuming it's in the first column)
                id_to_delete = tree.item(item, "values")[0]

                # Delete the item from the database
                cursor.execute("DELETE FROM STD1 WHERE ID=?", (id_to_delete,))
                conn.commit()

                tree.delete(item)





        btcnedit = Button(currentwindow)
        btcnedit.place(x=535, y=680) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ยกเลิกการจอง2.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=delete_selected)
        btcnedit.image = img8

        showstd1()       
        # เรียกใช้ฟังก์ชัน showstd1() เพื่อสร้าง Treeview

        
    def std2():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')     

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\UpdateSTD2.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)

        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=foradmin)
        Button1.image = img7   

        def showstd2():
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM STD2")
            data = cursor.fetchall()
            for row in data:
                tree.insert("", "end", values=row)

        # สร้าง Treeview
        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date", "Time", "Status"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")
        tree.heading("Status", text="Status")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)
        tree.column("Time", anchor="center", width=100)
        tree.column("Status", anchor="center", width=100)

        def update_status():
            selected_item = tree.selection()[0]
            new_status = status_combo.get()
            tree.item(selected_item, values=(tree.item(selected_item)['values'][0], tree.item(selected_item)['values'][1], tree.item(selected_item)['values'][2], tree.item(selected_item)['values'][3], tree.item(selected_item)['values'][4], new_status))

            # Update the database with the new status
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE STD2 SET status2 = ? WHERE id = ?", (new_status, tree.item(selected_item)['values'][0]))
            conn.commit()
            conn.close()
            
        # Create Combobox for Status
        status_combo = ttk.Combobox(currentwindow, values=["Paid", "Not Paid"],state="readonly")
        status_combo.place(x=435, y=635)


        btcnedit = Button(currentwindow)
        btcnedit.place(x=612, y=635 ,width=110, height=31) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonregยืนยันข้อมูล2.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=update_status)
        btcnedit.image = img8



        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)   
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)



        
        def delete_selected():
            # Get the selected item(s) in the Treeview widget
            selected_items = tree.selection()

            if not selected_items:
                messagebox.showwarning("No Selection", "กรุณาเลือกแถวที่ต้องการยกเลิกการจอง")
                return

            # Prompt the user for confirmation
            confirm = messagebox.askyesno("แจ้งเตือน", "คุณต้องการยกเลิกการจองนี้หรือไม่")

            if not confirm:
                return  # User chose not to delete

            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()

            for item in selected_items:
                # Get the ID (assuming it's in the first column)
                id_to_delete = tree.item(item, "values")[0]

                # Delete the item from the database
                cursor.execute("DELETE FROM STD2 WHERE ID=?", (id_to_delete,))
                conn.commit()

                tree.delete(item)

        btcnedit = Button(currentwindow)
        btcnedit.place(x=535, y=680) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ยกเลิกการจอง2.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=delete_selected)
        btcnedit.image = img8

        

        showstd2()
            
        
    def std3():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico')

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\UpdateSTD3.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)

        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=foradmin)
        Button1.image = img7          

        def showstd3():
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM STD3")
            data = cursor.fetchall()
            for row in data:
                tree.insert("", "end", values=row)

        # สร้าง Treeview
        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date", "Time", "Status"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")
        tree.heading("Status", text="Status")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)
        tree.column("Time", anchor="center", width=100)
        tree.column("Status", anchor="center", width=100)

        def update_status():
            selected_item = tree.selection()[0]
            new_status = status_combo.get()
            tree.item(selected_item, values=(tree.item(selected_item)['values'][0], tree.item(selected_item)['values'][1], tree.item(selected_item)['values'][2], tree.item(selected_item)['values'][3], tree.item(selected_item)['values'][4], new_status))

            # Update the database with the new status
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE STD3 SET status3 = ? WHERE id = ?", (new_status, tree.item(selected_item)['values'][0]))
            conn.commit()
            conn.close()
            
        status_combo = ttk.Combobox(currentwindow, values=["Paid", "Not Paid"],state="readonly")
        status_combo.place(x=435, y=635)


        btcnedit = Button(currentwindow)
        btcnedit.place(x=612, y=635 ,width=110, height=31) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonregยืนยันข้อมูล2.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=update_status)
        btcnedit.image = img8
            
            
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)   
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)
        
        def delete_selected():
            # Get the selected item(s) in the Treeview widget
            selected_items = tree.selection()

            if not selected_items:
                messagebox.showwarning("No Selection", "กรุณาเลือกแถวที่ต้องการยกเลิกการจอง")
                return

            # Prompt the user for confirmation
            confirm = messagebox.askyesno("แจ้งเตือน", "คุณต้องการยกเลิกการจองนี้หรือไม่")

            if not confirm:
                return  # User chose not to delete

            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            cursor = conn.cursor()

            for item in selected_items:
                # Get the ID (assuming it's in the first column)
                id_to_delete = tree.item(item, "values")[0]

                # Delete the item from the database
                cursor.execute("DELETE FROM STD3 WHERE ID=?", (id_to_delete,))
                conn.commit()

                tree.delete(item)

        btcnedit = Button(currentwindow)
        btcnedit.place(x=535, y=680) 
        btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
        img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ยกเลิกการจอง2.png")
        btcnedit.configure(image=img8)
        btcnedit.configure(command=delete_selected)
        btcnedit.image = img8

        
        showstd3()       

    
    def checkmoney():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico') 

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\BGเช็คยอดSTD1.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)

        #กดเพื่อหน้าหลัก 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button หน้าหลัก.png")
        Button1.configure(image=img7)
        Button1.configure(command=foradmin)
        Button1.image = img7  

         #กดเพื่อไปหน้าถัดไป 
        Button1 = Button(currentwindow)
        Button1.place(x=800,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ต่อไป.png")
        Button1.configure(image=img6)
        Button1.configure(command=checkmoney2)
        Button1.image = img6
    
        def checkmoneystd1():
            global year_combobox
            global month_combobox
            global total_label
            
            if year_combobox and month_combobox:
                selected_year = year_combobox.get()
                selected_month = month_combobox.get()
                
                # Clear the existing Treeview
                for item in tree.get_children():
                    tree.delete(item)

                conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM STD1 WHERE status1 = 'Paid' AND year = ? AND month = ?", (selected_year, selected_month))
                data = cursor.fetchall()

                for row in data:
                    tree.insert('', 'end', values=row)

                number_of_ids = len(tree.get_children())
                total_amount = number_of_ids * 800

                formatted_total_amount = f"{total_amount:,}"  # This formats the number with commas
                total_label = Label(currentwindow, text=f"จำนวนเงินรวมทั้งสิ้น: {formatted_total_amount} บาท ", font=("DB HELVETHAICA X BD EXT", 20), bg='white')
                total_label.place(x=435, y=690)

        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)   
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)
        

        def showmoneystd1():
            global year_combobox  # Declare year_combobox as a global variable
            year_combobox = ttk.Combobox(currentwindow, values=["2023", "2024", "2025"],state="readonly",width=4)
            year_combobox.place(x=457, y=226)

            global month_combobox  # Declare month_combobox as a global variable
            month_combobox = ttk.Combobox(currentwindow, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],state="readonly",width=4)
            month_combobox.place(x=591, y=226)
            
            #ยืนยันการเลือกดู
            btconf = Button(currentwindow)
            btconf.place(x=670, y=225) 
            btconf.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
            img1 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
            btconf.configure(image=img1)
            btconf.configure(command=checkmoneystd1)
            btconf.image = img1
            

        showmoneystd1()
        

    def checkmoney2():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico') 

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\BGเช็คยอดSTD2.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)

        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=checkmoney)
        Button1.image = img7  
       
        #กดเพื่อไปหน้าถัดไป 
        Button1 = Button(currentwindow)
        Button1.place(x=800,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ต่อไป.png")
        Button1.configure(image=img6)
        Button1.configure(command=checkmoney3)
        Button1.image = img6
        
        def checkmoneystd2():
            global year_combobox
            global month_combobox
            global total_label
            
            if year_combobox and month_combobox:
                selected_year = year_combobox.get()
                selected_month = month_combobox.get()
                
                # Clear the existing Treeview
                for item in tree.get_children():
                    tree.delete(item)

                conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM STD2 WHERE status2 = 'Paid' AND year = ? AND month = ?", (selected_year, selected_month))
                data = cursor.fetchall()

                for row in data:
                    tree.insert('', 'end', values=row)

                number_of_ids = len(tree.get_children())
                total_amount = number_of_ids * 1000

                formatted_total_amount = f"{total_amount:,}"  # This formats the number with commas
                total_label = Label(currentwindow, text=f"จำนวนเงินรวมทั้งสิ้น: {formatted_total_amount} บาท ", font=("DB HELVETHAICA X BD EXT", 20), bg='white')
                total_label.place(x=435, y=690)

        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        tree.place(x=100, y=280,width=935, height=300)
        vsb.place(x=1035, y=280, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1) 

        

        

        def showmoneystd2():
            global year_combobox  # Declare year_combobox as a global variable
            year_combobox = ttk.Combobox(currentwindow, values=["2023", "2024", "2025"],state="readonly",width=4)
            year_combobox.place(x=457, y=226)

            global month_combobox  # Declare month_combobox as a global variable
            month_combobox = ttk.Combobox(currentwindow, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],state="readonly",width=4)
            month_combobox.place(x=591, y=226)
            
            #ยืนยันการเลือกดู
            btconf = Button(currentwindow)
            btconf.place(x=670, y=225) 
            btconf.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
            img1 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
            btconf.configure(image=img1)
            btconf.configure(command=checkmoneystd2)
            btconf.image = img1

          
            

        showmoneystd2()

    
    def checkmoney3():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico') 

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\BGเช็คยอดSTD3.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)

        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=checkmoney2)
        Button1.image = img7  
       
        #กดเพื่อไปหน้าถัดไป 
        Button1 = Button(currentwindow)
        Button1.place(x=800,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ต่อไป.png")
        Button1.configure(image=img6)
        Button1.configure(command=checkmoneyall)
        Button1.image = img6
        
        def checkmoneystd3():
            global year_combobox
            global month_combobox
            global total_label
            
            if year_combobox and month_combobox:
                selected_year = year_combobox.get()
                selected_month = month_combobox.get()
                
                # Clear the existing Treeview
                for item in tree.get_children():
                    tree.delete(item)

                conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM STD3 WHERE status3 = 'Paid' AND year = ? AND month = ?", (selected_year, selected_month))
                data = cursor.fetchall()

                for row in data:
                    tree.insert('', 'end', values=row)

                number_of_ids = len(tree.get_children())
                total_amount = number_of_ids * 3500

                formatted_total_amount = f"{total_amount:,}"  # This formats the number with commas
                total_label = Label(currentwindow, text=f"จำนวนเงินรวมทั้งสิ้น: {formatted_total_amount} บาท ", font=("DB HELVETHAICA X BD EXT", 20), bg='white')
                total_label.place(x=435, y=690)

        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)    
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)
        

        def showmoneystd3():
            global year_combobox  # Declare year_combobox as a global variable
            year_combobox = ttk.Combobox(currentwindow, values=["2023", "2024", "2025"],state="readonly",width=4)
            year_combobox.place(x=457, y=226)

            global month_combobox  # Declare month_combobox as a global variable
            month_combobox = ttk.Combobox(currentwindow, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],state="readonly",width=4)
            month_combobox.place(x=591, y=226)
            
            #ยืนยันการเลือกดู
            btconf = Button(currentwindow)
            btconf.place(x=670, y=225) 
            btconf.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
            img1 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
            btconf.configure(image=img1)
            btconf.configure(command=checkmoneystd3)
            btconf.image = img1

            

        showmoneystd3()


    def checkmoneyall():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico') 

        currentwindow_bg= tk.PhotoImage(file=r"E:\PythonPJ\PythonPJ\BGเช็คยอดSTD1-3.png")
        bg_label=tk.Label(currentwindow,image=currentwindow_bg)
        bg_label.image = currentwindow_bg
        bg_label.place(x=0,y=0)

        #กดเพื่อย้อนกลับ 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ย้อนกลับ.png")
        Button1.configure(image=img7)
        Button1.configure(command=checkmoney3)
        Button1.image = img7  

        def checkmoneybill():
            global year_combobox
            global month_combobox
            global total_label

            if year_combobox and month_combobox:
                selected_year = year_combobox.get()
                selected_month = month_combobox.get()

                # Clear the existing Treeview
                for item in tree.get_children():
                    tree.delete(item)

                conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
                cursor = conn.cursor()

                # Fetch data from STD1 where status1 = 'Paid' and year/month match
                cursor.execute("SELECT * FROM STD1 WHERE status1 = 'Paid' AND year = ? AND month = ?", (selected_year, selected_month))
                data1 = cursor.fetchall()

                # Fetch data from STD2 where status2 = 'Paid' and year/month match
                cursor.execute("SELECT * FROM STD2 WHERE status2 = 'Paid' AND year = ? AND month = ?", (selected_year, selected_month))
                data2 = cursor.fetchall()

                # Fetch data from STD3 where status3 = 'Paid' and year/month match
                cursor.execute("SELECT * FROM STD3 WHERE status3 = 'Paid' AND year = ? AND month = ?", (selected_year, selected_month))
                data3 = cursor.fetchall()

                # Combine data from all three tables into one list
                all_data = data1 + data2 + data3
                totaldata1=len(data1)
                totaldata2=len(data2)
                totaldata3=len(data3)
                price1=800*totaldata1
                price2=1000*totaldata2
                price3=3500*totaldata3
                totalprice=price1+price2+price3
                formatted_total_amount = f"{totalprice:,}"  # This formats the number with commas
                total_label = Label(currentwindow, text=f"จำนวนเงินรวมทั้งสิ้น: {formatted_total_amount} บาท ", font=("DB HELVETHAICA X BD EXT", 20), bg='white')
                total_label.place(x=435, y=690)
                
                for row in all_data:
                    tree.insert('', 'end', values=row)
                
        tree = ttk.Treeview(currentwindow, columns=("ID", "Name", "Studio", "Date"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Studio", text="Studio")
        tree.heading("Date", text="Date")

        tree.column("ID", anchor="center", width=50)
        tree.column("Name", anchor="center", width=100)
        tree.column("Studio", anchor="center", width=100)
        tree.column("Date", anchor="center", width=100)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("DB HELVETHAICA X BD EXT", 25))
        tree.place(x=100, y=280,width=935, height=300)
        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)    
        vsb = ttk.Scrollbar(currentwindow, orient="vertical", command=tree.yview)
        tree.configure(yscroll=vsb.set)
        vsb.place(x=1035, y=280, height=300)
        
        def showmoneyall():
            global year_combobox  # Declare year_combobox as a global variable
            year_combobox = ttk.Combobox(currentwindow, values=["2023", "2024", "2025"],state="readonly",width=4)
            year_combobox.place(x=457, y=226)

            global month_combobox  # Declare month_combobox as a global variable
            month_combobox = ttk.Combobox(currentwindow, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],state="readonly",width=4)
            month_combobox.place(x=591, y=226)
            
            #ยืนยันการเลือกดู
            btconf = Button(currentwindow)
            btconf.place(x=670, y=225) 
            btconf.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
            img1 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
            btconf.configure(image=img1)
            btconf.configure(command=checkmoneybill)
            btconf.image = img1

    
            

        showmoneyall()

    
    #หน้าแก้ไข
    def update_user_info():
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        currentwindow = Tk()
        currentwindow.title("KHANTEP STUDIO")
        currentwindow.geometry("1135x880+450+80")
        currentwindow.iconbitmap('KhantepStudio.ico') 
        

        
        img = Image.open("E:\PythonPJ\PythonPJ\Windowsแก้ไขข้อมูลผู้ใช้.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo
        
        #กดเพื่อหน้าหลัก 
        Button1 = Button(currentwindow)
        Button1.place(x=180,y=750 ) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button หน้าหลัก.png")
        Button1.configure(image=img7)
        Button1.configure(command=foradmin)
        Button1.image = img7 

        #LOGOKHANTEP
        btlogo = Button(currentwindow)
        btlogo.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
        btlogo.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        btlogo.configure(image=img7)
        btlogo.configure(command=foradmin)
        btlogo.image = img7
        
        def edit1():
            idcard = idcardEntry.get()
            conn = sqlite3.connect('E:/PythonPJ/PythonPJ/khantepStudio1_data.db')
            c = conn.cursor()
            c.execute("SELECT username FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            if not booked:
                messagebox.showerror("Not Found", "ไม่พบข้อมูลที่ท่านกรอก")
                return
            for x in booked :
                    usnentry=Entry(currentwindow,textvariable=usn,width = 13,borderwidth=0,font=("DB Helvethaica X", 14))
                    usnentry.insert(0,x)
                    usnentry.place(x=465,y=280)
            c.execute("SELECT password FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    pwentry=Entry(currentwindow,textvariable=pw,width = 13,borderwidth=0,font=("DB Helvethaica X", 14))
                    pwentry.insert(0,x)
                    pwentry.place(x=480 ,y=340)
            c.execute("SELECT name FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    name_value = x[0].strip()
                    nentry = Entry(currentwindow, textvariable=n, width=13, borderwidth=0, font=("DB Helvethaica X", 14))
                    nentry.insert(0, name_value)
                    nentry.place(x=480, y=410)
            c.execute("SELECT IDCard FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    idcEntry=Entry(currentwindow,textvariable=idc,width = 13,borderwidth=0,font=("DB Helvethaica X", 14))
                    idcEntry.insert(0,x)
                    idcEntry.place(x=590 ,y=376)
            c.execute("SELECT phone FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    telentry=Entry(currentwindow,textvariable=tel,width = 13,borderwidth=0,font=("DB Helvethaica X", 14))
                    telentry.insert(0,x)
                    telentry.place(x=520 ,y=450) 
            c.execute("SELECT home_number FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    hnentry=Entry(currentwindow,textvariable=hn,width = 4,borderwidth=0,font=("DB Helvethaica X", 14))
                    hnentry.insert(0,x)
                    hnentry.place(x=465 ,y=525)

            c.execute("SELECT m FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    mentry=Entry(currentwindow,textvariable=m,width = 4,borderwidth=0,font=("DB Helvethaica X", 14))
                    mentry.insert(0,x)
                    mentry.place(x=585 ,y=525)

            c.execute("SELECT s FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    sentry=Entry(currentwindow,textvariable=s,width = 5,borderwidth=0,font=("DB Helvethaica X", 14))
                    sentry.insert(0,x)
                    sentry.place(x=720 ,y=525)
            
            c.execute("SELECT r FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    rentry=Entry(currentwindow,textvariable=r,width = 5,borderwidth=0,font=("DB Helvethaica X", 14))
                    rentry.insert(0,x)
                    rentry.place(x=420 ,y=560)

            c.execute("SELECT d FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    dentry=Entry(currentwindow,textvariable=d,width = 5,borderwidth=0,font=("DB Helvethaica X", 14))
                    dentry.insert(0,x)
                    dentry.place(x=580 ,y=563)

            c.execute("SELECT dis FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    disentry=Entry(currentwindow,textvariable=dis,width = 7,borderwidth=0,font=("DB Helvethaica X", 14))
                    disentry.insert(0,x)
                    disentry.place(x=440 ,y=603)

            c.execute("SELECT pro FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    proentry=Entry(currentwindow,textvariable=pro,width = 7,borderwidth=0,font=("DB Helvethaica X", 14))
                    proentry.insert(0,x)
                    proentry.place(x=645 ,y=602)

            c.execute("SELECT pi FROM register WHERE idcard=?", (idcard,))
            booked = c.fetchall()
            for x in booked :
                    pientry=Entry(currentwindow,textvariable=pi,width = 7,borderwidth=0,font=("DB Helvethaica X", 14))
                    pientry.insert(0,x)
                    pientry.place(x=510 ,y=643)
            

            def saveedit():
                usn = usnentry.get()
                pw = pwentry.get()
                n = nentry.get()
                idc = idcEntry.get()
                tel = telentry.get()
                hn = hnentry.get()
                m = mentry.get()
                s = sentry.get()
                r = rentry.get()
                d = dentry.get()
                dis = disentry.get()
                pro = proentry.get()
                pi = pientry.get()
                idcard=idcardEntry.get()

                data = (usn, pw, n, idc, tel, hn, m, s, r, d, dis, pro, pi,idcard)
                c.execute('''UPDATE register SET username=?, password=?, name=?, IDcard=?, phone=?, home_number=?, m=?, s=?, r=?, d=?, dis=?, pro=?, pi=? WHERE IDcard=?''', data)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "ข้อมูลถูกอัปเดตเรียบร้อย")

                foradmin()

            btcnedit = Button(currentwindow)
            btcnedit.place(relx=0.588, rely=0.8 ,width=122, height=31) 
            btcnedit.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
            img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonregยืนยันข้อมูล2.png")
            btcnedit.configure(image=img8)
            btcnedit.configure(command=saveedit)
            btcnedit.image = img8

            def delete_data():
                idcard = idcardEntry.get()
                conn = sqlite3.connect('E:/PythonPJ/PythonPJ/khantepStudio1_data.db')
                c = conn.cursor()
                
                if not booked:
                    messagebox.showerror("Not Found", "ไม่พบข้อมูล")
                else:
                    confirmation = messagebox.askyesno("Confirmation", "คุณต้องการลบหรือไม่")
                    if confirmation:
                        c.execute("DELETE FROM register WHERE IDcard=?", (idcard,))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success", "ลบข้อมูลสำเร็จ")

                        usnentry.delete(0, END)
                        pwentry.delete(0, END)
                        nentry.delete(0, END)
                        idcEntry.delete(0, END)
                        telentry.delete(0, END)
                        hnentry.delete(0, END)
                        mentry.delete(0, END)
                        sentry.delete(0, END)
                        rentry.delete(0, END)
                        dentry.delete(0, END)
                        disentry.delete(0, END)
                        proentry.delete(0, END)
                        pientry.delete(0, END)

            # Create the "Delete" button
            btcnedit = Button(currentwindow)
            btcnedit.place(relx=0.390, rely=0.8 ,width=125, height=31) 
            btcnedit.configure(relief="flat",overrelief="flat",activebackground="#d53c3c",cursor="hand2",foreground="#d53c3c",background="#d53c3c",borderwidth='0')
            img8 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\ลบข้อมูล.png")
            btcnedit.configure(image=img8)
            btcnedit.configure(command=delete_data)
            btcnedit.image = img8
            

        # Define idcardEntry as an Entry widget
        idcardEntry = Entry(currentwindow, width=30, font=25, bd=0)
        idcardEntry.place(x=410, y=775)
        
        btSch = Button(currentwindow)
        btSch.place(relx=0.612, rely=0.878 ,width=37, height=27) 
        btSch.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img7 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonค้นหา.png")
        btSch.configure(image=img7)
        btSch.configure(command=edit1)
        btSch.image = img7

        
   
    btedit = Button(currentwindow)
    btedit.place(relx=0.215, rely=0.4219 ,width=300, height=55) 
    btedit.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonประวัติการจอง.png")
    btedit.configure(image=img1)
    btedit.configure(command=history)
    btedit.image = img1
    
    btstd1 = Button(currentwindow)
    btstd1.place(relx=0.525, rely=0.4219 ,width=300, height=55) 
    btstd1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Button updateSTD1.png")
    btstd1.configure(image=img2)
    btstd1.configure(command=std1)
    btstd1.image = img2

    btstd2 = Button(currentwindow)
    btstd2.place(relx=0.525, rely=0.525 ,width=300, height=55) 
    btstd2.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Button updateSTD2.png")
    btstd2.configure(image=img3)
    btstd2.configure(command=std2)
    btstd2.image = img3

    btstd3 = Button(currentwindow)
    btstd3.place(relx=0.525, rely=0.630 ,width=300, height=55) 
    btstd3.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Button updateSTD3.png")
    btstd3.configure(image=img4)
    btstd3.configure(command=std3)
    btstd3.image = img4

    btcheckmoney = Button(currentwindow)
    btcheckmoney.place(relx=0.215, rely=0.630 ,width=300, height=55) 
    btcheckmoney.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonตรวจสอบยอดเงิน.png")
    btcheckmoney.configure(image=img5)
    btcheckmoney.configure(command=checkmoney)
    btcheckmoney.image = img5

    btupdate_user = Button(currentwindow)
    btupdate_user.place(relx=0.215, rely=0.525 ,width=300, height=55) 
    btupdate_user.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonแก้ไขข้อมูลผู้ใช้.png")
    btupdate_user.configure(image=img6)
    btupdate_user.configure(command=update_user_info)
    btupdate_user.image = img6
    
HomePage ()

currentwindow.mainloop()
