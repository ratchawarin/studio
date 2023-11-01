from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkinter import ttk

try:
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
    # conn.close()
except sqlite3.Error as e:
    messagebox.showerror("Database Error", str(e))

    
def homePage():
    global current_window
    

# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')

# Background
    img = Image.open(r"E:\PythonPJ\PythonPJ\BG2.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window,image=photo)
    lbl.pack()
    lbl.image = photo       # เก็บ reference รูป

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
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
    Button1.configure(command=contact)
    Button1.image = img4

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7
    
#login
    Button1 = Button(current_window)
    Button1.place(relx=0.388, rely=0.832 ,width=105, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button login12.png")
    Button1.configure(image=img5)
    Button1.configure(command=login)
    Button1.image = img5

#rge
    Button1 = Button(current_window)
    Button1.place(relx=0.543, rely=0.832 ,width=143, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img6 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button reg.png")
    Button1.configure(image=img6)
    Button1.configure(command=registerPage)
    Button1.image = img6



    current_window.mainloop()

    # if current_window:
    #     current_window.destroy()



    
    



###############################################Windowcontact##################################################
def contact():
    global current_window
    if current_window:
        current_window.destroy()

# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')

# Background
    img = Image.open("BGติดต่อ.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
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
    Button1.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
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
    Button1.configure(command=contact)
    Button1.image = img4
    
#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7


#############################################Windowcheck##################################################
def check():
    global current_window
    if current_window:
        current_window.destroy()

# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')

# Background
    img = Image.open("E:\PythonPJ\PythonPJ\BGเช็ดตารางห้อง.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
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
    Button1.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
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
    Button1.configure(command=contact)
    Button1.image = img4
    
#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7


###############################################windowslogin#################################################
def login():
    
    global current_window,registerEntry

    if current_window:
        current_window.destroy()

    def fetch_user_data():
        username = registerEntry.get()
        password = passwordEntry.get()

        user_data = get_user_data(username, password)

    def ServiceStudio1():
        def windowconfirm1():
            global windowpopup2,current_window
            
        # Setting หน้าจอโปรแกรม
            windowpopup2 = Toplevel(current_window)
            windowpopup2.title("KHANTEP STUDIO")
            windowpopup2.geometry("520x520+750+300")
            windowpopup2.iconbitmap('KhantepStudio.ico')
            
        #BG ทั้งหมด
            img = Image.open("E:\PythonPJ\PythonPJ\WindowใบจองSelf-ServiceStudio.png")       
            photo = ImageTk.PhotoImage(img)
            lbl = Label(windowpopup2, image=photo)
            lbl.pack()
            lbl.image = photo

        #Exit
            Button1 = Button(windowpopup2)
            Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
            Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
            img5 = PhotoImage(file=r"ButtonExit.png")
            Button1.configure(image=img5)
            
            Button1.image = img5

            conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM register")
            name = cursor.fetchall()
            Label(windowpopup2,text=name,bg='#ffffff',font=20).place(x=200,y=125)


    
        global current_window
        if current_window:
            current_window.destroy()
            current_window = Tk()
        # Setting หน้าจอโปรแกรม
            current_window.title("KHANTEP STUDIO")
            current_window.geometry("1135x880+450+80")
            current_window.iconbitmap('KhantepStudio.ico')
        
        


    #BG ทั้งหมด
        img = Image.open(r"E:\PythonPJ\PythonPJ\BGSelf-ServiceStudio1.png")       
        photo = ImageTk.PhotoImage(img)
        lbl = Label(current_window, image=photo)
        lbl.pack()
        lbl.image = photo

    #LOGOKHANTEP
        Button1 = Button(current_window)
        Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
        Button1.configure(image=img1)
        Button1.configure(command=homePage)
        Button1.image = img1

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
        Button1.configure(command=contact)
        Button1.image = img4

    #กดเพื่อจอง
        Button1 = Button(current_window)
        Button1.place(relx=0.69, rely=0.315 ,width=80, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
        img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\Buttonจองเลย.png")
        Button1.configure(image=img5)
        Button1.configure(command=windowconfirm1)
        
        Button1.image = img5

    #กดเพื่อไปหน้าถัดไป 
        Button1 = Button(current_window)
        Button1.place(relx=0.876, rely=0.82 ,width=30, height=25) 
        Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
        img6 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonหน้าถัดไป.png")
        Button1.configure(image=img6)
        
        Button1.image = img6

    def get_user_data(username, password):
        try:
            conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM register")
            user_data = cursor.fetchall()
            user = []
            if username and password:
                for x,y in user_data:
                    if x == username:
                        if y ==password:
                            usernametrue = str(x)
                            messagebox.showinfo("Login Successful", "Welcome, " +usernametrue)
                            
    
                            global current_window
                            if current_window:
                                current_window.destroy()

                        # Setting หน้าจอโปรแกรม
                            current_window = Tk()
                            current_window.title("KHANTEP STUDIO")
                            current_window.geometry("1135x880+450+80")
                            current_window.iconbitmap('KhantepStudio.ico')

                            

                        # Background
                            img = Image.open("BG3AfterLogin.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
                            photo = ImageTk.PhotoImage(img)
                            lbl = Label(current_window, image=photo)
                            lbl.pack()
                            lbl.image = photo       # เก็บ reference รูป

                        #เลือกจองห้อง
                            Button1 = Button(current_window)
                            Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
                            Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
                            img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เลือกจองห้อง.png")
                            Button1.configure(image=img2)
                            Button1.configure(command=ServiceStudio1)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
                            Button1.image = img2

                        #เช็คตารางห้อง
                            Button1 = Button(current_window)
                            Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
                            Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
                            img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
                            Button1.configure(image=img3)
                            Button1.configure(command=homePage)
                            Button1.image = img3

                        #วิธีการจอง
                            Button1 = Button(current_window)
                            Button1.place(relx=0.48, rely=0.015 ,width=175, height=52) 
                            Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
                            img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
                            Button1.configure(image=img4)
                            Button1.configure(command=homePage)
                            Button1.image = img4

                        #ติดต่อ
                            Button1 = Button(current_window)
                            Button1.place(relx=0.65, rely=0.015 ,width=175, height=52) 
                            Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
                            img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
                            Button1.configure(image=img5)
                            Button1.configure(command=homePage)
                            Button1.image = img5

                        #LOGOKHANTEP
                            Button1 = Button(current_window)
                            Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
                            Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
                            img7 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
                            Button1.configure(image=img7)
                            Button1.configure(command=homePage)
                            Button.image = img7


                            
                            

                            Label(current_window,text=username,font=20,bg='#ffffff').place(x=600,y=730)




                        else:
                            messagebox.showerror("Login Failed", "Invalid username or password")
                    user.append(x)                      
                if username not in user:
                    messagebox.showerror("Login Failed", "Invalid username or password")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
            return None

# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')

#BG ทั้งหมด
    img = Image.open("E:\PythonPJ\PythonPJ\BGLogin.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.000, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

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

    registerEntry=Entry(current_window,width=25,font=25,bd=0)
    registerEntry.place(x=520,y=425)

    passwordEntry=Entry(current_window,width=25,font=25,bd=0)
    passwordEntry.place(x=520,y=480)
        

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4



#ยืนยันเข้าสู่ระบบ
    Button1 = Button(current_window)
    Button1.place(relx=0.613, rely=0.597 ,width=80, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#0c00a5",cursor="hand2",foreground="#0c00a5",background="#0c00a5",borderwidth='0')
    img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
    Button1.configure(image=img5)
    Button1.configure(command=fetch_user_data)
    Button1.image = img5

###############################################windowsRegisterPage#################################################


def registerPage():
    global current_window, registerEntry, passwordEntry, nameEntry, telEntry, homenbEntry, mEntry, sEntry, rEntry, dEntry, disEntry, proEntry, piEntry

    if current_window:
        current_window.destroy()

    def handle_register_confirm_click():
        global name

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

        # Check if the username already exists in the database
        conn = sqlite3.connect("E:/PythonPJ/PythonPJ/usertest_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM register WHERE username=?", (username,))
        existing_username = cursor.fetchone()

        if existing_username:
            messagebox.showerror("Error", "มีคนใช้ username นี้ไปแล้ว")
        elif not (username and password and name and phone and home_number and m and s and r and d and dis and pro and pi):
            messagebox.showerror("Error", "กรุณากรอกให้ครบทุกช่อง")
        else:
            # Insert the new user into the database
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

            

# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("E:\PythonPJ\PythonPJ\BG1Reg.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=check)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
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
    Button1.configure(command=contact)
    Button1.image = img4

#ยืนยันการสมัครสมาชิก
    Button1 = Button(current_window)
    Button1.place(relx=0.64, rely=0.757 ,width=122, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/BGReg/buttonregCF.png")
    Button1.configure(image=img5)
    Button1.configure(command=handle_register_confirm_click)
    Button1.image = img5   

########

    registerEntry=Entry(current_window,width=30,font=25,bd=0)
    registerEntry.place(x=395,y=328)

    passwordEntry=Entry(current_window,width=25,font=25,bd=0)
    passwordEntry.place(x=415,y=387)

    nameEntry=Entry(current_window,width=25,font=25,bd=0)
    nameEntry.place(x=403,y=430)

    telEntry=Entry(current_window,width=25,font=25,bd=0)
    telEntry.place(x=438,y=475)

    homenbEntry=Entry(current_window,width=6,font=25,bd=0)
    homenbEntry.place(x=390,y=542)

    mEntry=Entry(current_window,width=7,font=25,bd=0)
    mEntry.place(x=515,y=542)

    sEntry=Entry(current_window,width=7,font=25,bd=0)
    sEntry.place(x=645,y=542)

    rEntry=Entry(current_window,width=7,font=25,bd=0)
    rEntry.place(x=780,y=542)

    dEntry=Entry(current_window,width=11,font=25,bd=0)
    dEntry.place(x=365,y=575)

    disEntry=Entry(current_window,width=9,font=25,bd=0)
    disEntry.place(x=566,y=575)

    proEntry=Entry(current_window,width=9,font=25,bd=0)
    proEntry.place(x=754,y=575)

    piEntry=Entry(current_window,width=9,font=25,bd=0)
    piEntry.place(x=430,y=611)

    
    
homePage()


