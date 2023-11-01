# from tkinter import *
# from PIL import Image, ImageTk
# import sqlite3
# from tkinter import messagebox
# from tkinter import ttk

# conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
# cursor = conn.cursor()

# try:
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS register (
    #     id integer PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,name TEXT,phone TEXT,
    #     home_number TEXT,m TEXT,s TEXT,r TEXT,d TEXT,dis TEXT,pro TEXT,pi TEXT
    #         )
    #     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS STD1 (
#         id integer PRIMARY KEY AUTOINCREMENT,date TEXT,
#         month TEXT,years TEXT,date2 TEXT,month2 TEXT,years2 TEXT
#             )
#         """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS STD2 (
#         id integer PRIMARY KEY AUTOINCREMENT,date TEXT,month TEXT,years TEXT,
#         date2 TEXT,month2 TEXT,years2 TEXT
#             )
#         """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS STD3 (
#         id integer PRIMARY KEY AUTOINCREMENT,
#         date TEXT,month TEXT,years TEXT,date2 TEXT,month2 TEXT,years2 TEXT
#             )
#         """)

#     conn.commit()
#     # conn.close()
# except sqlite3.Error as e:
#     messagebox.showerror("Database Error", str(e))



from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkinter import ttk

currentwindow = None

def registerPage():
    
    global currentwindow
    showtel = ''
    if currentwindow:
        currentwindow.destroy()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')

    
    def regis():
        username = registerEntry.get()
        password = passwordEntry.get()
        name = nameEntry.get()
        phone = telEntry.get()
        home_number = homenbEntry.get()
        m = mEntry.get()
        s = sEntry.get()
        r = rEntry.get()
        d = dEntry.get()
        dis = disEntry.get()
        pro = proEntry.get()
        pi = piEntry.get()
        phone = showtel
        conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM register WHERE username=?", (username,))
        existing_username = cursor.fetchone()
    # เพิ่มเงื่อนไขตรวจสอบว่ามีช่องใดช่องหนึ่งไม่ได้กรอกข้อมูลเข้าไป
        if not (username and password and name and phone and home_number and m and s and r and d and dis and pro and pi):
            messagebox.showerror("Error", "กรุณากรอกให้ครบทุกช่อง")
        else:
            conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM register WHERE username=?", (username,))
            existing_username = cursor.fetchone()

            if existing_username:
                messagebox.showerror("Error", "มีคนใช้ username นี้ไปแล้ว")
                registerEntry.delete(0,END)
            else:
                cursor.execute(
                    "INSERT INTO register (username, password, name, phone, home_number, m, s, r, d, dis, pro, pi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (username, password, name, phone, home_number, m, s, r, d, dis, pro, pi),
                )
                cursor.execute("INSERT INTO STD1(date,month,years,date2,month2,years2) VALUES (?,?,?,?,?,?)",
                    (0, 0, 0, 0, 0, 0))
                cursor.execute("INSERT INTO STD2(date,month,years,date2,month2,years2) VALUES (?,?,?,?,?,?)",
                    (0, 0, 0, 0, 0, 0))
                cursor.execute("INSERT INTO STD3(date,month,years,date2,month2,years2) VALUES (?,?,?,?,?,?)",
                    (0, 0, 0, 0, 0, 0))
                conn.commit()
                messagebox.showinfo("Success", "Registration successful!")
                
                
                login()

            


    
    img = Image.open("E:\PythonPJ\PythonPJ\BG1Reg.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(currentwindow, image=photo)
    lbl.pack()
    lbl.image = photo

    

    registerEntry=Entry(currentwindow,width=30,font=25,bd=0)
    registerEntry.place(x=395,y=328)

    passwordEntry=Entry(currentwindow,width=25,font=25,bd=0)
    passwordEntry.place(x=415,y=387)

    nameEntry=Entry(currentwindow,width=25,font=25,bd=0)
    nameEntry.place(x=403,y=430)

    telEntry=Entry(currentwindow,width=25,font=25,bd=0)
    telEntry.place(x=438,y=475)

    homenbEntry=Entry(currentwindow,width=6,font=25,bd=0)
    homenbEntry.place(x=390,y=542)

    mEntry=Entry(currentwindow,width=7,font=25,bd=0)
    mEntry.place(x=515,y=542)

    sEntry=Entry(currentwindow,width=7,font=25,bd=0)
    sEntry.place(x=645,y=542)

    rEntry=Entry(currentwindow,width=7,font=25,bd=0)
    rEntry.place(x=780,y=542)

    dEntry=Entry(currentwindow,width=11,font=25,bd=0)
    dEntry.place(x=365,y=575)

    disEntry=Entry(currentwindow,width=9,font=25,bd=0)
    disEntry.place(x=566,y=575)

    proEntry=Entry(currentwindow,width=9,font=25,bd=0)
    proEntry.place(x=754,y=575)

    piEntry=Entry(currentwindow,width=9,font=25,bd=0)
    piEntry.place(x=430,y=611)

#ยืนยันการสมัคร
    btsubreg = Button(currentwindow)
    btsubreg.place(relx=0.64, rely=0.757 ,width=122, height=19) 
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
    #ประกาศตัวแปรเก็บค่าไปใช้
    logged_in_name=''
    showtel = ''
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

    
    
    
    def authenticate():
        nonlocal logged_in_name  
        nonlocal showtel
        username = registerEntry.get()
        password = passwordEntry.get()

        conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM register WHERE username=? AND password=?", (username, password))
        log = c.fetchone()
    
        if log:
            logged_in_name = log[3] 
            showtel=log[4] # Store the logged-in user's name
            messagebox.showinfo("Login Successful", "Welcome, " + logged_in_name)
            homepage2()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            login()
            
    registerEntry = Entry( currentwindow,width=25,font=25,bd=0)
    registerEntry.place(x=520,y=425)

    passwordEntry = Entry( currentwindow, width=25,font=25,bd=0)
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
    #     btbooking.configure(command=homePage)
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

        img = Image.open("E:\PythonPJ\PythonPJ\BGเช็ดตารางห้อง.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
        photo = ImageTk.PhotoImage(img)
        lbl = Label(currentwindow, image=photo)
        lbl.pack()
        lbl.image = photo       # เก็บ reference รูป

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

    #วิธีการจอง
        Button1 = Button(currentwindow)
        Button1.place(relx=0.48, rely=0.015 ,width=175, height=52) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
        Button1.configure(image=img4)
        # Button1.configure(command=HomePage)
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
        Button1.configure(command=HomePage)
        Button.image = img7






    def Bookingstu1():
        nonlocal logged_in_name
        global currentwindow
        if currentwindow:
            currentwindow.destroy()
        
        
        
        def windowconfirm1():
                global currentwindow,windowpopup1
                nonlocal showtel 
                
            # Setting หน้าจอโปรแกรม
                windowpopup1 = Toplevel(currentwindow)
                windowpopup1.title("KHANTEP STUDIO")
                windowpopup1.geometry("520x520+750+300")
                windowpopup1.iconbitmap('KhantepStudio.ico')
                
            #BG ทั้งหมด
                conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
                cursor = conn.cursor()

                # Fetch the "d" value from the "register" table
                
                #Nameuser,Phonenumber
                name_user = str()
                phone = str()
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if str(x[3]) == str(logged_in_name):
                        name_user = str(x[3])
                        phone = str(x[4])   
                


                
                   
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
                name_userShow = Label(windowpopup1, text=f' {name_user}',bg='white',font=25,bd=0 )
                name_userShow.place(x=125,y=130)
                phoneNumber_label = Label(windowpopup1, text=f' {phone}', bg='white',font=25,bd=0)
                phoneNumber_label.place(x=155, y=170)
                
                cal_label = Label(windowpopup1, text="วันที่จอง : ", bg='white', font=("Arial", 14))
                cal_label.place(x=400, y=280)
                cal = Calendar(windowpopup1, selectmode="day", year=2023, month=9, day=10)
                cal.place(x=550, y=280)

                

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
                # if currentwindow:
                #     currentwindow.destroy()
                # Setting หน้าจอโปรแกรม
                windowpopup2 = Toplevel(currentwindow)
                windowpopup2.title("KHANTEP STUDIO")
                windowpopup2.geometry("520x520+750+300")
                windowpopup2.iconbitmap('KhantepStudio.ico')
            #BG ทั้งหมด

                conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
                cursor = conn.cursor()

                #phomnuber
                phoneNumber = str()
                # print(logged_in_name)
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if str(x[1]) == logged_in_name:
                        phoneNumber = str(x[4])
                #nameuser
                name_user = ()
                # print(name_user)
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if (x[1]) == logged_in_name:
                        name_user = (x[3])



                img = Image.open("WindowใบจองMini Studio.png")       
                photo = ImageTk.PhotoImage(img)
                lbl = Label(windowpopup2, image=photo)
                lbl.pack()
                lbl.image = photo

                #เรียกชื่อกับเบอร์โทรมาแสดง
                name_user = Label(windowpopup2, text=f' {name_user}',bg='white',font=25,bd=0 )
                name_user.place(x=125,y=130)
                phoneNumber_label = Label(windowpopup2, text=f' {phoneNumber}', bg='white',font=25,bd=0)
                phoneNumber_label.place(x=155, y=170)

                #Exit
                Button1 = Button(windowpopup2)
                Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
                img5 = PhotoImage(file=r"ButtonExit.png")
                Button1.configure(command=HomePage)
                Button1.configure(image=img5)
                Button1.image = img5    
                
                #ยืนยันการจอง
                Button1 = Button(windowpopup2)
                Button1.place(relx=0.83, rely=0.82 ,width=80, height=19) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
                img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/buttonregยืนยันการจอง.png")
                Button1.configure(image=img5)
                Button1.configure(command=windowconfirm2)
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
                # if currentwindow:
                #     currentwindow.destroy()
                # Setting หน้าจอโปรแกรม
                windowpopup3 = Toplevel(currentwindow)
                windowpopup3.title("KHANTEP STUDIO")
                windowpopup3.geometry("520x520+750+300")
                windowpopup3.iconbitmap('KhantepStudio.ico')
            #BG ทั้งหมด

                conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
                cursor = conn.cursor()

                # Fetch the "d" value from the "register" table
                phoneNumber = str()
                # print(logged_in_name)
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if str(x[1]) == logged_in_name:
                        phoneNumber = str(x[4])
                #ืNameuser
                name_user = ()
                # print(name_user)
                cursor.execute("SELECT * FROM register")
                data = cursor.fetchall()
                for x in data:
                    if (x[1]) == logged_in_name:
                        name_user = (x[3])


                
                img = Image.open("WindowใบจองMainStudio.png")       
                photo = ImageTk.PhotoImage(img)
                lbl = Label(windowpopup3, image=photo)
                lbl.pack()
                lbl.image = photo

                #เรียกชื่อกับเบอร์โทรมาแสดง
                name_user = Label(windowpopup3, text=f' {name_user}',bg='white',font=25,bd=0 )
                name_user.place(x=125,y=130)
                phoneNumber_label = Label(windowpopup3, text=f' {phoneNumber}', bg='white',font=25,bd=0)
                phoneNumber_label.place(x=155, y=170)


                #Exit
                Button1 = Button(windowpopup3)
                Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
                img5 = PhotoImage(file=r"ButtonExit.png")
                Button1.configure(command=HomePage)
                Button1.configure(image=img5)
                Button1.image = img5    
                
                

                #ยืนยันการจอง
                Button1 = Button(windowpopup3)
                Button1.place(relx=0.83, rely=0.82 ,width=80, height=19) 
                Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
                img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/buttonregยืนยันการจอง.png")
                Button1.configure(image=img5)
                Button1.configure(command=windowconfirm3)
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
        # Button1.configure(command=contact)
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
    #    btbooking.configure(command=homePage)
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



def check():
    global currentwindow
    if currentwindow:
        currentwindow.destroy ()
    currentwindow = Tk()
    currentwindow.title("KHANTEP STUDIO")
    currentwindow.geometry("1135x880+450+80")
    currentwindow.iconbitmap('KhantepStudio.ico')
    img = Image.open(r"E:\PythonPJ\PythonPJ\BGเช็ดตารางห้อง.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
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



HomePage ()

currentwindow.mainloop()