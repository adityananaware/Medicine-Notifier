import sqlite3

def create_tables():
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS medicines (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        expiry_date TEXT NOT NULL,
                        purchase_date TEXT NOT NULL,
                        duration INTEGER NOT NULL)''')

    conn.commit()
    conn.close()

def add_medicine(name, expiry_date, purchase_date, duration):
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medicines (name, expiry_date, purchase_date, duration) VALUES (?, ?, ?, ?)", 
                   (name, expiry_date, purchase_date, duration))
    conn.commit()
    conn.close()

def fetch_medicines():
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    data = cursor.fetchall()
    conn.close()
    return data

create_tables()
