import sqlite3
from datetime import datetime, date

# -------------------------------
# DATABASE INITIALIZATION
# -------------------------------
def init_db():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()

    # Create Students table
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dept TEXT,
            year INTEGER,
            contact TEXT,
            guardian TEXT,
            guardian_contact TEXT,
            room_no TEXT
        )
    """)

    # Create Entry Logs table
    c.execute("""
        CREATE TABLE IF NOT EXISTS entry_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            entry_time TEXT,
            exit_time TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # Create Medical Info table
    c.execute("""
        CREATE TABLE IF NOT EXISTS medical_info (
            student_id INTEGER PRIMARY KEY,
            blood_group TEXT,
            allergies TEXT,
            conditions TEXT,
            emergency_contact TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # Create Leave Requests table
    c.execute("""
        CREATE TABLE IF NOT EXISTS leave_requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            from_date TEXT,
            to_date TEXT,
            reason TEXT,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# STUDENT FUNCTIONS
# -------------------------------
def add_student(name, dept, year, contact, guardian, guardian_contact, room_no):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO students (name, dept, year, contact, guardian, guardian_contact, room_no)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, dept, year, contact, guardian, guardian_contact, room_no))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return data

def delete_student(student_id):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    c.execute("DELETE FROM entry_logs WHERE student_id=?", (student_id,))
    c.execute("DELETE FROM leave_requests WHERE student_id=?", (student_id,))
    c.execute("DELETE FROM medical_info WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()


# -------------------------------
# ENTRY LOG FUNCTIONS
# -------------------------------
def add_entry(student_id, entry_time=None, exit_time=None, status="On Time"):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    if not entry_time:
        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""
        INSERT INTO entry_logs (student_id, entry_time, exit_time, status)
        VALUES (?, ?, ?, ?)
    """, (student_id, entry_time, exit_time, status))
    conn.commit()
    conn.close()

def view_logs():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM entry_logs")
    data = c.fetchall()
    conn.close()
    return data


# -------------------------------
# MEDICAL INFO FUNCTIONS
# -------------------------------
def add_medical_info(student_id, blood_group, allergies, conditions, emergency_contact):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO medical_info 
        (student_id, blood_group, allergies, conditions, emergency_contact)
        VALUES (?, ?, ?, ?, ?)
    """, (student_id, blood_group, allergies, conditions, emergency_contact))
    conn.commit()
    conn.close()

def view_medical_info(student_id):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM medical_info WHERE student_id=?", (student_id,))
    data = c.fetchone()
    conn.close()
    return data


# -------------------------------
# LEAVE REQUEST FUNCTIONS
# -------------------------------
def add_leave_request(student_id, from_date, to_date, reason):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO leave_requests (student_id, from_date, to_date, reason)
        VALUES (?, ?, ?, ?)
    """, (student_id, from_date, to_date, reason))
    conn.commit()
    conn.close()

def view_leave_requests():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM leave_requests")
    data = c.fetchall()
    conn.close()
    return data

def update_leave_status(request_id, new_status):
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("UPDATE leave_requests SET status=? WHERE request_id=?", (new_status, request_id))
    conn.commit()
    conn.close()


# -------------------------------
# RUN DATABASE INITIALIZATION & DEMO DATA
# -------------------------------
if __name__ == "__main__":
    init_db()
    print("✅ Database initialized successfully!")

    import random

    # --- Add demo students ---
    sample_students = [
        ("Aarav Sharma", "CSE", 2, "9876543210", "Ramesh Sharma", "9123456789", "A-101"),
        ("Priya Patel", "ECE", 3, "9988776655", "Suresh Patel", "9090909090", "B-202"),
        ("Rohan Mehta", "ME", 1, "7896541230", "Nilesh Mehta", "8564237890", "C-103"),
        ("Isha Verma", "CSE", 4, "9658741235", "Sanjay Verma", "8899776655", "A-104"),
        ("Karan Gupta", "IT", 2, "9012345678", "Manoj Gupta", "9543217890", "A-105"),
        ("Simran Kaur", "CIVIL", 3, "9876501234", "Balbir Kaur", "9456123789", "D-106"),
        ("Aditya Nair", "EEE", 1, "9898123456", "Rajeev Nair", "9789654123", "E-107"),
        ("Neha Singh", "CSE", 2, "9812345670", "Amit Singh", "9021345678", "A-108"),
        ("Rahul Das", "ECE", 4, "9900123456", "Dipak Das", "9999888877", "B-109"),
        ("Tanya Jain", "CIVIL", 1, "9876123450", "Ravi Jain", "9765432109", "D-110"),
        ("Vikram Rao", "ME", 3, "9908765432", "Suresh Rao", "9556677889", "C-111"),
        ("Sneha Reddy", "CSE", 2, "9823456781", "Anil Reddy", "9445566778", "A-112"),
        ("Devansh Thakur", "IT", 4, "9798123455", "Rohit Thakur", "9123098765", "B-113"),
        ("Meera Pillai", "EEE", 3, "9800123499", "Gopal Pillai", "9876500012", "E-114"),
        ("Arjun Yadav", "CIVIL", 2, "9912345678", "Mahesh Yadav", "9456123098", "D-115"),
    ]

    for s in sample_students:
        try:
            add_student(*s)
        except:
            pass

    print("✅ Added 15 demo students")

    # --- Add demo logs ---
    for sid in range(1, 16):
        for _ in range(random.randint(1, 3)):
            entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            add_entry(sid, entry_time, None, random.choice(["Checked-In", "Checked-Out", "On Time"]))

    print("✅ Added demo entry logs")

    # --- Add demo leave requests ---
    for sid in range(1, 11):
        start = date.today()
        end = date.today()
        reason = random.choice(["Festival", "Medical", "Family Function", "Competition", "Personal Work"])
        add_leave_request(sid, str(start), str(end), reason)
        update_leave_status(sid, random.choice(["Approved", "Rejected", "Pending"]))

    print("✅ Added demo leave requests")
