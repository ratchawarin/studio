from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

# Connect to the SQLite database
conn = sqlite3.connect("E:/PythonPJ/PythonPJ/user_data.db")
cursor = conn.cursor()

def homePage():
    # Add logic for navigating to the home page
    pass

# Function to fetch user data from the database
def fetch_user_data(username, password):
    try:
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user_data = cursor.fetchone()
        return user_data
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
        return None

# Function to handle login
def login2():
    # Retrieve the username and password from the entry fields
    username = registerEntry.get()
    password = passwordEntry.get()

    # Check if the username and password match the data in the database
    user_data = fetch_user_data(username, password)

    if user_data:
        # If user is found in the database, show a login success message
        messagebox.showinfo("Login Successful", "Welcome, " + username)
        # You can perform additional actions or navigation here
    else:
        # If user is not found, show an error message
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
windows1 = Tk()
windows1.title("KHANTEP STUDIO")
windows1.geometry("1135x880+450+80")
windows1.iconbitmap('KhantepStudio.ico')

# Load and display the background image
img = Image.open(r"E:\PythonPJ\PythonPJ\BGReg\BGLogin.jpg")
photo = ImageTk.PhotoImage(img)
lbl = Label(image=photo)
lbl.pack()  

#ข้อความ
registerEntry=Entry(windows1,width=25,font=25,bd=0)
registerEntry.place(x=520,y=425)

passwordEntry=Entry(windows1,width=25,font=25,bd=0)
passwordEntry.place(x=520,y=480)



# Create and configure the logo button
Button_logo = Button(windows1)
Button_logo.place(relx=0.001, rely=0.0019, width=100, height=65)
Button_logo.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img1 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\logo1.png")
Button_logo.configure(image=img1)
Button_logo.configure(command=homePage)
Button_logo.image = img1

# เช็คตารางห้อง
Button_check_schedule = Button(windows1)
Button_check_schedule.place(relx=0.09, rely=0.015, width=175, height=52)
Button_check_schedule.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img2 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button เช็คตารางห้อง.png")
Button_check_schedule.configure(image=img2)
Button_check_schedule.configure(command=homePage)
Button_check_schedule.image = img2

# วิธีการจองห้อง
Button_how_to_book = Button(windows1)
Button_how_to_book.place(relx=0.275, rely=0.015, width=175, height=52)
Button_how_to_book.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img3 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button วิธีการจองห้อง.png")
Button_how_to_book.configure(image=img3)
Button_how_to_book.configure(command=homePage)
Button_how_to_book.image = img3

# ติดต่อ
Button_contact = Button(windows1)
Button_contact.place(relx=0.42, rely=0.015, width=175, height=52)
Button_contact.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img4 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\button ติดต่อ.png")
Button_contact.configure(image=img4)
Button_contact.configure(command=homePage)
Button_contact.image = img4

# ยืนยันเข้าสู่ระบบ  
Button_login_confirm = Button(windows1, command=login2)  # Set the login function as the command
Button_login_confirm.place(relx=0.613, rely=0.597, width=80, height=19)
Button_login_confirm.configure(relief="flat", overrelief="flat", activebackground="#0d00b2", cursor="hand2", foreground="#0d00b2", background="#0d00b2", borderwidth='0')
img5 = PhotoImage(file=r"E:\PythonPJ\PythonPJ\buttonLoginCF\buttonLoginCF.png")
Button_login_confirm.configure(image=img5)
Button_login_confirm.image = img5

# ... (rest of your code)

# Start the Tkinter main loop
windows1.mainloop()
