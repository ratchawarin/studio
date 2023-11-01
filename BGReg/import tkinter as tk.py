import tkinter as tk
from tkinter import ttk

def calculate_duration():
    start_day = int(start_day_combobox.get())
    start_month = int(start_month_combobox.get())
    start_year = int(start_year_combobox.get())
    
    end_day = int(end_day_combobox.get())
    end_month = int(end_month_combobox.get())
    end_year = int(end_year_combobox.get())
    
    start_date = f"{start_year}-{start_month:02d}-{start_day:02d}"
    end_date = f"{end_year}-{end_month:02d}-{end_day:02d}"
    
    # ทำงานกับ start_date และ end_date ตามที่คุณต้องการ
    # เช่น คำนวณระยะเวลา หรือประมวลผลข้อมูล

app = tk.Tk()
app.title("คำนวณระยะเวลา")

# สร้าง combobox สำหรับวัน เดือน และปีเริ่มต้น
start_day_combobox = ttk.Combobox(app, values=list(range(1, 32)))
start_day_combobox.set(1)  # ตั้งค่าเริ่มต้นให้เป็นวันที่ 1
start_day_combobox.grid(row=0, column=0)

start_month_combobox = ttk.Combobox(app, values=list(range(1, 13)))
start_month_combobox.set(1)  # ตั้งค่าเริ่มต้นให้เป็นเดือนที่ 1
start_month_combobox.grid(row=0, column=1)

start_year_combobox = ttk.Combobox(app, values=list(range(2000, 2031)))
start_year_combobox.set(2022)  # ตั้งค่าเริ่มต้นให้เป็นปี 2022
start_year_combobox.grid(row=0, column=2)

# สร้าง combobox สำหรับวัน เดือน และปีสิ้นสุด
end_day_combobox = ttk.Combobox(app, values=list(range(1, 32)))
end_day_combobox.set(1)  # ตั้งค่าเริ่มต้นให้เป็นวันที่ 1
end_day_combobox.grid(row=1, column=0)

end_month_combobox = ttk.Combobox(app, values=list(range(1, 13)))
end_month_combobox.set(1)  # ตั้งค่าเริ่มต้นให้เป็นเดือนที่ 1
end_month_combobox.grid(row=1, column=1)

end_year_combobox = ttk.Combobox(app, values=list(range(2000, 2031)))
end_year_combobox.set(2022)  # ตั้งค่าเริ่มต้นให้เป็นปี 2022
end_year_combobox.grid(row=1, column=2)

calculate_button = tk.Button(app, text="คำนวณระยะเวลา", command=calculate_duration)
calculate_button.grid(row=2, columnspan=3)

app.mainloop()
