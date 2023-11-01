from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

# Function to save the selected date to the database
def save_date():
    selected_day1 = day1_combobox.get()
    selected_day2 = day2_combobox.get()
    selected_month = month_combobox.get()
    selected_year = year_combobox.get()

    # Insert the selected date into the database
    cursor.execute("INSERT INTO users (time, mont, name, pee) VALUES (?, ?, ?, ?)",
                   (f"{selected_day1} {selected_month} {selected_year}", selected_month, "", ""))
    conn.commit()
    messagebox.showinfo("Success", "Date saved to the database!")

# Create the main window
windows0 = Tk()
windows0.title("KHANTEP STUDIO")
windows0.geometry("1135x880+450+80")
windows0.iconbitmap('KhantepStudio.ico')

conn = sqlite3.connect("E:/PythonPJ/PythonPJ/use7r_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    time TEXT PRIMARY KEY,
    mont TEXT,
    name TEXT,
    pee TEXT
)
""")
conn.commit()

# Create lists for days, months, and years
days = [str(i) for i in range(1, 32)]
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]
years = [str(i) for i in range(1900, 2101)]

# Create combo boxes for day, month, and year
day1_combobox = ttk.Combobox(windows0, values=days, state="readonly")
day2_combobox = ttk.Combobox(windows0, values=days, state="readonly")
month_combobox = ttk.Combobox(windows0, values=months, state="readonly")
year_combobox = ttk.Combobox(windows0, values=years)

# Create a button to save the selected date
save_button = Button(windows0, text="Save Date", command=save_date)

# Pack the combo boxes and save button or use grid to place them in the desired location
day1_combobox.place(x=200,y=200)
day2_combobox.place(x=400,y=200)
month_combobox.pack()
year_combobox.pack()
save_button.pack()

# Run the Tkinter main loop
windows0.mainloop()
