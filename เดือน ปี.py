
#ใต้ check money
def filter_data():
            global year_combobox
            global month_combobox
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

        tree.grid(row=0, column=0, padx=50, pady=100, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        currentwindow.grid_rowconfigure(0, weight=1)
        currentwindow.grid_columnconfigure(0, weight=1)   

        def showmoneystd1():
            global year_combobox  # Declare year_combobox as a global variable
            year_combobox = ttk.Combobox(currentwindow, values=["2023", "2024", "2025"],state="readonly")
            year_combobox.place(x=400, y=100)

            global month_combobox  # Declare month_combobox as a global variable
            month_combobox = ttk.Combobox(currentwindow, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],state="readonly")
            month_combobox.place(x=500, y=100)
            filter_button = Button(currentwindow, text="Filter Data", command=filter_data)
            filter_button.place(x=600, y=100)