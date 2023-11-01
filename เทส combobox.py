def admin():
    global tree
    name=  ''
    idcard=''
    phone=''
    studio=''
    datead=''
    time=''
    tree = None


    currentwindow = Tk()
    currentwindow.title("Admin")
    currentwindow.geometry('1000x650+275+60')


    def on_vertical_scroll(*args):
            tree.yview(*args)
    tree_label = Label(currentwindow, text="ประวัติการจอง", font=("DB Helvethaica X", 14))
    tree_label.pack()
    frame = ttk.Frame(currentwindow)
    frame.pack()
    tree = ttk.Treeview(frame,columns=("id","name","IDcard","phone","studio","date","time"))
    tree.heading("id",text="id")
    tree.heading("name",text="ชื่อ")
    tree.heading("IDcard",text="บัตรประชาชน")
    tree.heading("phone",text="เบอร์")
    tree.heading("studio",text="ห้อง")
    tree.heading("date",text="วันที่จอง")
    tree.heading("time",text="เวลา")
    tree.column("id",anchor="center",width=60)
    tree.column("name",anchor="center",width=125)
    tree.column("IDcard",anchor="center",width=125)
    tree.column("phone",anchor="center",width=110)
    tree.column("studio",anchor="center",width=150)
    tree.column("date",anchor="center",width=100)
    tree.column("time",anchor="center",width=100)
    tree.column("#0",width=0,stretch=NO)
    style = ttk.Style()
    style.configure("Treeview.Heading",font = ("Arial",20))
    style.configure("Treeview", font=("DB Helvethaica X", 16))
    conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history ")
    result = c.fetchall()
    for x in result :
            tree.insert("","end",values=x)
    vscrollbar = ttk.Scrollbar(frame, orient="vertical", command=on_vertical_scroll)
    vscrollbar.pack(side="right", fill="y")
    tree.config(yscrollcommand=vscrollbar.set)
    tree.pack(fill="both", expand=True)        
    backadmin_But1=Button(currentwindow,text='ย้อนกลับ',command=lambda:(currentwindow.destroy(),login()),font=("DB Helvethaica X", 10),cursor="hand2")
    backadmin_But1.place(x=300,y=550)
    


    def edit_data():
        global tree  
        
        selected_item = tree.selection()  # Get the selected item in the Treeview

        if not selected_item:
            messagebox.showerror("Error", "กรุณาเลือกข้อมูลที่ต้องการแก้ไข")
            currentwindow.destroy()
            admin()
        
        selected_id = tree.item(selected_item, "values")[0]  # Get the ID of the selected row

        if not selected_id:
            messagebox.showerror("Error", "ไม่มีข้อมูลให้แก้ไข")
            currentwindow.destroy()
            admin()
        
        # Prompt the user to enter new data
        new_name = simpledialog.askstring("Edit Name", "Enter new name:")
        new_idcard = simpledialog.askstring("Edit ID Card", "Enter new ID card:")
        new_phone = simpledialog.askstring("Edit Phone", "Enter new phone:")
        new_studio = simpledialog.askstring("Edit Studio", "Enter new studio:")
        new_datead = simpledialog.askstring("Edit Date", "Enter new date:")
        new_time = simpledialog.askstring("Edit Time", "Enter new time:")

        if new_name is not None and new_idcard is not None and new_phone is not None and new_studio is not None and new_datead is not None and new_time is not None:
            # Update the record in the Treeview
            tree.item(selected_item, values=(selected_id, new_name, new_idcard, new_phone, new_studio, new_datead, new_time))
            currentwindow.destroy()
            
        # Update the record in the database
        conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
        c = conn.cursor()
        c.execute("UPDATE history SET name=?, IDcard=?, phone=?, studio=?, date=?, time=? WHERE id=?",
                  (new_name, new_idcard, new_phone, new_studio, new_datead, new_time, selected_id))
        conn.commit()
        conn.close()
            
    def delete_data():
        selected_item = tree.selection()  # Get the selected item in the Treeview

        if not selected_item:
            messagebox.showerror("Error", "No data selected for deletion")
            return

        selected_id = tree.item(selected_item, "values")[0]  # Get the ID of the selected row

        # Ask the user for confirmation
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this data?")

        if confirmation:
            # Connect to the database
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            c = conn.cursor()
            # Execute a DELETE query based on the selected ID
            c.execute("DELETE FROM history WHERE id=?", (selected_id,))
            conn.commit()
            conn.close()

            # Refresh the Treeview after deletion
            tree.delete(selected_item)
        else:
            # User selected "no," so do nothing or navigate back to the admin page
            currentwindow.destroy()
            admin()  # Reopen the admin page

    def delete_all_data():
    # Ask the user for confirmation
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete all data?")
        currentwindow.destroy()
        admin()
        if confirmation:
            # Connect to the database
            conn = sqlite3.connect("E:\PythonPJ\PythonPJ\khantepStudio1_data.db")
            c = conn.cursor()
            
            # Check if there's data to delete
            c.execute("SELECT COUNT(*) FROM history")
            count = c.fetchone()[0]
            
            if count > 0:
                # Execute a DELETE query to delete all data
                c.execute("DELETE FROM history")
                conn.commit()
                conn.close()

                # Clear the Treeview
                tree.delete(*tree.get_children())
            else:
                messagebox.showerror("Error", "ไม่มีข้อมูลในรายการที่จะลบ")
                currentwindow.destroy()
                admin()
              

    delete_button = Button(currentwindow, text="ลบข้อมูลทั้งหมด", command=delete_all_data, font=("DB Helvethaica X", 10), cursor="hand2")
    delete_button.place(x=550, y=550)

    delete_button = Button(currentwindow, text="ลบข้อมูล", command=delete_data, font=("DB Helvethaica X", 10), cursor="hand2")
    delete_button.place(x=400, y=550)
    
    edit_button = Button(currentwindow, text="แก้ไขข้อมูล", command=edit_data, font=("DB Helvethaica X", 10), cursor="hand2")
    edit_button.place(x=500, y=550)
                