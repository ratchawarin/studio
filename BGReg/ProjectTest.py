import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Global variable to keep track of the current window
current_window = None

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
    img = Image.open("BG1.png")        #คำสั่งรีไซต์รูปภาพ #ใส่ต่อด้านล่าง # img = img.resize((int(img.width * .5), int(img.height* .5)))
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.place(x = 0, y = 0)
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
    Button1.place(relx=0.388, rely=0.835 ,width=105, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#aaaaaa",cursor="hand2",foreground="#aaaaaa",background="#aaaaaa",borderwidth='0')
    img5 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button login12.png")
    Button1.configure(image=img5)
    Button1.configure(command=homePage)
    Button1.image = img5

#rge
    Button1 = Button(current_window)
    Button1.place(relx=0.543, rely=0.835 ,width=143, height=33) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#1100ed",cursor="hand2",foreground="#1100ed",background="#1100ed",borderwidth='0')
    img6 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\button reg.png")
    Button1.configure(image=img6)
    Button1.configure(command=registerPage)
    Button1.image = img6

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=70) 
    Button1.configure(relief="flat",overrelief="flat",activebackground="#000000",cursor="hand2",foreground="#000000",background="#000000",borderwidth='0')
    img7 = PhotoImage(file=r"C:\Users\danny\OneDrive\Desktop\PythonPJ\logo1.png")
    Button1.configure(image=img7)
    Button1.configure(command=homePage)
    Button.image = img7

def login():
    global current_window
    if current_window:
        current_window.destroy()
#เดี๋ยว GUI ตามมาค้าบบบบบ
#เดี๋ยว GUI ตามมาค้าบบบบบ    
#เดี๋ยว GUI ตามมาค้าบบบบบ    
#เดี๋ยว GUI ตามมาค้าบบบบบ

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
    img = Image.open("BG1_Reg.png")       
    photo = ImageTk.PhotoImage(img)
    lbl = Label(current_window, image=photo)
    lbl.place(x = 0, y = 0)
    lbl.image = photo

#LOGOKHANTEP
    Button1 = Button(current_window)
    Button1.place(relx=0.001, rely=0.0019 ,width=100, height=70) 
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
    Button1.configure(command=homePage)
    Button1.image = img5
    
    

# Initial call to show_window1 to start the application
homePage()
current_window.mainloop()
