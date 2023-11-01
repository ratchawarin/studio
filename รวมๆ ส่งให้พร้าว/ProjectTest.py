from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

# Global variable to keep track of the current window
current_window = None

conn = sqlite3.connect("C:/Users/danny/OneDrive/Desktop/PythonPJ/user22_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
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
conn.commit()




def homePage():
    global current_window
    if current_window:
        current_window.destroy()

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
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4
    
#login
    Button1 = Button(current_window)
    Button1.place(relx=0.388, rely=0.832 ,width=105, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button login12.png")
    Button1.configure(image=img5)
    Button1.configure(command=login)
    Button1.image = img5

#rge
    Button1 = Button(current_window)
    Button1.place(relx=0.543, rely=0.832 ,width=143, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img6 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button reg.png")
    Button1.configure(image=img6)
    Button1.configure(command=registerPage)
    Button1.image = img6

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7

def homePage2():
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
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เลือกจองห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=ServiceStudio1)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#วิธีการจอง
    Button1 = Button(current_window)
    Button1.place(relx=0.48, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.65, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage)
    Button1.image = img5

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.0, rely=0.0019 ,width=100, height=65) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7

###############################################windowslogin#################################################
def login():
    global current_window
    if current_window:
        current_window.destroy()
# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("BGLogin.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.000, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4

#ยืนยันเข้าสู่ระบบ
    Button1 = Button(current_window)
    Button1.place(relx=0.613, rely=0.597 ,width=80, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#0d00b2",cursor="hand2",foreground="#0d00b2",background="#0d00b2",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\BGLogin\buttonLoginCF.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage2)
    Button1.image = img5
    
###############################################windowsRegisterPage#################################################
def registerPage():
    global current_window
    if current_window:
        current_window.destroy()


# Setting หน้าจอโปรแกรม
    current_window = Tk()
    current_window.title("KHANTEP STUDIO")
    current_window.geometry("1135x880+450+80")
    current_window.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("BG1Reg.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4

#ยืนยันการสมัครสมาชิก
    Button1 = Button(current_window)
    Button1.place(relx=0.64, rely=0.757 ,width=122, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\BGReg\buttonregCF.png")
    Button1.configure(image=img5)
    Button1.configure(command=login)
    Button1.image = img5   

###############################################windowspopup#################################################
def Bookingstu1():
    global windowpopup,current_window
# Setting หน้าจอโปรแกรม
    windowpopup = Toplevel(current_window)
    windowpopup.title("KHANTEP STUDIO")
    windowpopup.geometry("570x170+750+450")
    windowpopup.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("windowbooking.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(windowpopup, image=photo)
    lbl.pack()
    lbl.image = photo

#ยืนยันการจอง
    Button1 = Button(windowpopup)
    Button1.place(relx=0.83, rely=0.82 ,width=80, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\buttonregยืนยันการจอง.png")
    Button1.configure(image=img5)
    Button1.configure(command=windowconfirm1)
    Button1.image = img5   

def windowconfirm1():
    global windowpopup2, windowpopup, current_window
    if windowpopup :
        windowpopup.destroy()
# Setting หน้าจอโปรแกรม
    windowpopup2 = Toplevel(current_window)
    windowpopup2.title("KHANTEP STUDIO")
    windowpopup2.geometry("520x520+750+300")
    windowpopup2.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("WindowใบจองSelf-ServiceStudio.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(windowpopup2, image=photo)
    lbl.pack()
    lbl.image = photo

#Exit
    Button1 = Button(windowpopup2)
    Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\ButtonExit.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage2)
    Button1.image = img5   


def Bookingstu2():
    global windowpopup,current_window
# Setting หน้าจอโปรแกรม
    windowpopup = Toplevel(current_window)
    windowpopup.title("KHANTEP STUDIO")
    windowpopup.geometry("570x170+750+450")
    windowpopup.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("windowbooking.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(windowpopup, image=photo)
    lbl.pack()
    lbl.image = photo

#ยืนยันการจอง
    Button1 = Button(windowpopup)
    Button1.place(relx=0.83, rely=0.82 ,width=80, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\buttonregยืนยันการจอง.png")
    Button1.configure(image=img5)
    Button1.configure(command=windowconfirm2)
    Button1.image = img5   

def windowconfirm2():
    global windowpopup2, windowpopup, current_window
    if windowpopup :
        windowpopup.destroy()
# Setting หน้าจอโปรแกรม
    windowpopup2 = Toplevel(current_window)
    windowpopup2.title("KHANTEP STUDIO")
    windowpopup2.geometry("520x520+750+300")
    windowpopup2.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("WindowใบจองMini Studio.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(windowpopup2, image=photo)
    lbl.pack()
    lbl.image = photo

#Exit
    Button1 = Button(windowpopup2)
    Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\ButtonExit.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage2)
    Button1.image = img5   

def Bookingstu3():
    global windowpopup,current_window
# Setting หน้าจอโปรแกรม
    windowpopup = Toplevel(current_window)
    windowpopup.title("KHANTEP STUDIO")
    windowpopup.geometry("570x170+750+450")
    windowpopup.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("windowbooking.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(windowpopup, image=photo)
    lbl.pack()
    lbl.image = photo

#ยืนยันการจอง
    Button1 = Button(windowpopup)
    Button1.place(relx=0.83, rely=0.82 ,width=80, height=19) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\buttonregยืนยันการจอง.png")
    Button1.configure(image=img5)
    Button1.configure(command=windowconfirm3)
    Button1.image = img5   

def windowconfirm3():
    global windowpopup2, windowpopup, current_window
    if windowpopup :
        windowpopup.destroy()
# Setting หน้าจอโปรแกรม
    windowpopup2 = Toplevel(current_window)
    windowpopup2.title("KHANTEP STUDIO")
    windowpopup2.geometry("520x520+750+300")
    windowpopup2.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("WindowใบจองMainStudio.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(windowpopup2, image=photo)
    lbl.pack()
    lbl.image = photo

#Exit
    Button1 = Button(windowpopup2)
    Button1.place(relx=0.9, rely=0.905 ,width=57, height=49) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\ButtonExit.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage2)
    Button1.image = img5  


###############################################windowsStudio#################################################
def ServiceStudio1():
    global current_window
    if current_window:
        current_window.destroy()
        current_window = Tk()
    # Setting หน้าจอโปรแกรม
        current_window.title("KHANTEP STUDIO")
        current_window.geometry("1135x880+450+80")
        current_window.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("BGSelf-ServiceStudio1.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4

#กดเพื่อจอง
    Button1 = Button(current_window)
    Button1.place(relx=0.69, rely=0.315 ,width=80, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\Buttonจองเลย.png")
    Button1.configure(image=img5)
    Button1.configure(command=Bookingstu1)
    Button1.image = img5

#กดเพื่อไปหน้าถัดไป 
    Button1 = Button(current_window)
    Button1.place(relx=0.876, rely=0.82 ,width=30, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img6 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\buttonหน้าถัดไป.png")
    Button1.configure(image=img6)
    Button1.configure(command=MiniStudio)
    Button1.image = img6    

def MiniStudio():
    global current_window
    if current_window:
        current_window.destroy()
        current_window = Tk()
    # Setting หน้าจอโปรแกรม
        current_window.title("KHANTEP STUDIO")
        current_window.geometry("1135x880+450+80")
        current_window.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("BGMiniStudio.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4

#กดเพื่อจอง
    Button1 = Button(current_window)
    Button1.place(relx=0.61, rely=0.315 ,width=80, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\Buttonจองเลย.png")
    Button1.configure(image=img5)
    Button1.configure(command=Bookingstu2)
    Button1.image = img5

#กดเพื่อไปหน้าถัดไป 
    Button1 = Button(current_window)
    Button1.place(relx=0.876, rely=0.82 ,width=30, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img6 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\buttonหน้าถัดไป.png")
    Button1.configure(image=img6)
    Button1.configure(command=MainStudio)
    Button1.image = img6

#กดเพื่อย้อนกลับ 
    Button1 = Button(current_window)
    Button1.place(relx=0.159, rely=0.82 ,width=30, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\buttonย้อนกลับ.png")
    Button1.configure(image=img7)
    Button1.configure(command=ServiceStudio1)
    Button1.image = img7


def MainStudio():
    global current_window
    if current_window:
        current_window.destroy()
        current_window = Tk()
    # Setting หน้าจอโปรแกรม
        current_window.title("KHANTEP STUDIO")
        current_window.geometry("1135x880+450+80")
        current_window.iconbitmap('KhantepStudio.ico')
    
#BG ทั้งหมด
    img = Image.open("BGMainStudio.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.pack()
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=60) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img1 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img1)
    Button1.configure(command=homePage)
    Button1.image = img1

#เช็คตารางห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.09, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img2 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button เช็คตารางห้อง.png")
    Button1.configure(image=img2)
    Button1.configure(command=homePage)         # ลิงก์ไปหน้า หรือฟังก์ชั่นอื่น
    Button1.image = img2

#วิธีการจองห้อง
    Button1 = Button(current_window)
    Button1.place(relx=0.275, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img3 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button วิธีการจองห้อง.png")
    Button1.configure(image=img3)
    Button1.configure(command=homePage)
    Button1.image = img3

#ติดต่อ
    Button1 = Button(current_window)
    Button1.place(relx=0.42, rely=0.015 ,width=175, height=52) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img4 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button ติดต่อ.png")
    Button1.configure(image=img4)
    Button1.configure(command=homePage)
    Button1.image = img4

#กดเพื่อจอง
    Button1 = Button(current_window)
    Button1.place(relx=0.6, rely=0.315 ,width=80, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#ee5b5e",cursor="hand2",foreground="#ee5b5e",background="#ee5b5e",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\Buttonจองเลย.png")
    Button1.configure(image=img5)
    Button1.configure(command=Bookingstu3)
    Button1.image = img5

#กดเพื่อย้อนกลับ 
    Button1 = Button(current_window)
    Button1.place(relx=0.159, rely=0.82 ,width=30, height=25) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img6 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\image Studio\buttonย้อนกลับ.png")
    Button1.configure(image=img6)
    Button1.configure(command=MiniStudio)
    Button1.image = img6




    
    

# Initial call to show_window1 to start the application
homePage()
current_window.mainloop()
