from tkinter import *
from PIL import Image, ImageTk

# Create the main window
windows2 = Tk()
windows2.title("KHANTEP STUDIO")
windows2.geometry("1135x880+450+80")
windows2.iconbitmap('KhantepStudio.ico')









# Load and display the background image
img = Image.open("E:/PythonPJ/PythonPJ/BGReg/BG1_Reg.png")
photo = ImageTk.PhotoImage(img)
lbl = Label(image=photo)
lbl.pack()

#ข้อความ
registerEntry=Entry(windows2,width=30,font=25,bd=0)
registerEntry.place(x=395,y=328)

passwordEntry=Entry(windows2,width=25,font=25,bd=0)
passwordEntry.place(x=415,y=387)

nameEntry=Entry(windows2,width=25,font=25,bd=0)
nameEntry.place(x=403,y=430)

telEntry=Entry(windows2,width=25,font=25,bd=0)
telEntry.place(x=438,y=475)

homenbEntry=Entry(windows2,width=6,font=25,bd=0)
homenbEntry.place(x=390,y=542)

mEntry=Entry(windows2,width=7,font=25,bd=0)
mEntry.place(x=515,y=542)

sEntry=Entry(windows2,width=7,font=25,bd=0)
sEntry.place(x=645,y=542)

rEntry=Entry(windows2,width=7,font=25,bd=0)
rEntry.place(x=780,y=542)

dEntry=Entry(windows2,width=11,font=25,bd=0)
dEntry.place(x=365,y=575)

disEntry=Entry(windows2,width=9,font=25,bd=0)
disEntry.place(x=566,y=575)

proEntry=Entry(windows2,width=9,font=25,bd=0)
proEntry.place(x=754,y=575)

piEntry=Entry(windows2,width=9,font=25,bd=0)
piEntry.place(x=430,y=611)

#LOGOKHANTEP
def handle_logo_click():
    # Add your logo button click logic here
    pass

Button_logo = Button(windows2, command=handle_logo_click)
Button_logo.place(relx=0.001, rely=0.0001, width=100, height=70)
Button_logo.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img1 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/logo1.png")
Button_logo.configure(image=img1)

#เช็คตารางห้อง
def handle_check_schedule_click():
    # Add your check schedule button click logic here
    pass

Button_check_schedule = Button(windows2, command=handle_check_schedule_click)
Button_check_schedule.place(relx=0.09, rely=0.01, width=175, height=52)
Button_check_schedule.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img2 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button เช็คตารางห้อง.png")
Button_check_schedule.configure(image=img2)

#วิธีการจองห้อง
def handle_how_to_book_click():
    # Add your how to book button click logic here
    pass

Button_how_to_book = Button(windows2, command=handle_how_to_book_click)
Button_how_to_book.place(relx=0.275, rely=0.01, width=175, height=52)
Button_how_to_book.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img3 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button วิธีการจองห้อง.png")
Button_how_to_book.configure(image=img3)

#ยืนยันการสมัครสมาชิก
def handle_register_confirm_click():
    # Add your register confirm button click logic here
    pass

Button_register_confirm = Button(windows2, command=handle_register_confirm_click)
Button_register_confirm.place(relx=0.639, rely=0.755, width=122, height=19)
Button_register_confirm.configure(relief="flat", overrelief="flat", activebackground="#1100ed", cursor="hand2", foreground="#1100ed", background="#1100ed", borderwidth='0')
img4 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/BGReg/buttonregCF.png")
Button_register_confirm.configure(image=img4)

#ติดต่อ
def handle_contact_click():
    # Add your contact button click logic here
    pass

Button_contact = Button(windows2, command=handle_contact_click)
Button_contact.place(relx=0.42, rely=0.01, width=175, height=52)
Button_contact.configure(relief="flat", overrelief="flat", activebackground="#000000", cursor="hand2", foreground="#000000", background="#000000", borderwidth='0')
img5 = PhotoImage(file=r"E:/PythonPJ/PythonPJ/button ติดต่อ.png")
Button_contact.configure(image=img5)

# Start the Tkinter main loop
windows2.mainloop()
