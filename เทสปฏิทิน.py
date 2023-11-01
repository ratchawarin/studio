def admin():
                admin_window = Toplevel(root)
                admin_window.title("Admin")
                admin_window.geometry('1000x650+275+60')
                def on_vertical_scroll(*args):
                        tree.yview(*args)
                tree_label = tk.Label(admin_window, text="ข้อมูล users ทั้งหมด", font=("DB Helvethaica X", 14))
                tree_label.pack()
                frame = ttk.Frame(admin_window)
                frame.pack()
                tree = ttk.Treeview(frame,columns=("id","name","lastname","tel","email","password"))
                tree.heading("id",text="id")
                tree.heading("name",text="ชื่อ")
                tree.heading("lastname",text="นามสกุล")
                tree.heading("tel",text="เบอร์")
                tree.heading("email",text="อีเมล")
                tree.heading("password",text="รหัส")
                tree.column("id",anchor="center",width=60)
                tree.column("name",anchor="center",width=125)
                tree.column("lastname",anchor="center",width=125)
                tree.column("tel",anchor="center",width=110)
                tree.column("email",anchor="center",width=150)
                tree.column("password",anchor="center",width=100)
                tree.column("#0",width=0,stretch=NO)
                style = ttk.Style()
                style.configure("Treeview.Heading",font = ("Arial",12))
                style.configure("Treeview", font=("DB Helvethaica X", 12))
                conn = sqlite3.connect("registers.db")
                c = conn.cursor()
                c.execute("SELECT * FROM users ")
                result = c.fetchall()
                for x in result :
                        tree.insert("","end",values=x)
                vscrollbar = ttk.Scrollbar(frame, orient="vertical", command=on_vertical_scroll)
                vscrollbar.pack(side="right", fill="y")
                tree.config(yscrollcommand=vscrollbar.set)
                tree.pack(fill="both", expand=True)
                admin_But1=Button(admin_window,text='แก้ไขข้อมูลและสถานะการจอง', command=lambda:(update(),admin_window.destroy()), font=("DB Helvethaica X", 10),cursor="hand2")
                admin_But1.place(x=360,y=550)
                Button(admin_window, text="เคลียร์ตารางงาน", bg='#fcd3e2', command=lambda: (delete_booking()), font=("DB Helvethaica X", 10),cursor="hand2").place(x=300, y=590)   
                     
                backadmin_But1=Button(admin_window,text='ย้อนกลับ',command=lambda:(admin_window.destroy(),login()),font=("DB Helvethaica X", 10),cursor="hand2")
                backadmin_But1.place(x=300,y=550)
                def on_vertical_scroll(*args):
                        tree.yview(*args) 
                tree_label = tk.Label(admin_window, text="ข้อมูลการจอง", font=("DB Helvethaica X", 14))
                tree_label.pack()
                frame1 = ttk.Frame(admin_window)
                frame1.pack()
                tree = ttk.Treeview(frame1,columns=("id","email","package","booking_date","address","status"))
                tree.heading("id",text="")
                tree.heading("email",text="อีเมลล์")
                tree.heading("package",text="แพ็คเกต")
                tree.heading("booking_date",text="วันที่จอง")
                tree.heading("address",text="สถานที่จัดงาน")
                tree.heading("status",text="สถานะ")
                tree.column("id",anchor="center",width=60)
                tree.column("email",anchor="center",width=150)
                tree.column("package",anchor="center",width=100)
                tree.column("booking_date",anchor="center",width=80)
                tree.column("address",anchor="center",width=150)
                tree.column("status",anchor="center",width=130)
                tree.column("#0",width=0,stretch=NO)
                style = ttk.Style()
                style.configure("Treeview.Heading",font = ("Arial", 12))
                style.configure("Treeview", font=("DB Helvethaica X", 12))
                conn = sqlite3.connect("registers.db")
                c = conn.cursor()
                c.execute("SELECT * FROM booking ")
                result = c.fetchall()
                for x in result :
                        tree.insert("","end",values=x)
                vscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=on_vertical_scroll)
                vscrollbar.pack(side="right", fill="y")
                tree.config(yscrollcommand=vscrollbar.set)
                tree.pack(fill="both", expand=True)
                def delete_booking():
                                conn = sqlite3.connect('registers.db')
                                c = conn.cursor()
                                c.execute("DELETE FROM data ")
                                conn.commit()
                                conn.close()