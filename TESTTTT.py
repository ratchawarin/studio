
import sqlite3
conn = sqlite3.connect("E:/PythonPJ/PythonPJ/khantepStudio1_data.db")
cursor = conn.cursor()
cursor.execute("SELECT day,month,Year FROM STD1 WHERE id = 4 ", )
existing_record = cursor.fetchone()
i = []
for i in existing_record:
    print(i[0])