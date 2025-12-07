import sqlite3

# connect to database (creates hostel.db file if it doesn’t exist)
conn = sqlite3.connect('hostel.db')
c = conn.cursor()

# 1️⃣ Student Table
c.execute('''
CREATE TABLE IF NOT EXISTS Student(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    year INTEGER,
    contact_no TEXT,
    guardian_name TEXT,
    guardian_contact TEXT,
    room_no TEXT
)
''')

# 2️⃣ Entry/Exit Log Table
c.execute('''
CREATE TABLE IF NOT EXISTS EntryLog(
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    entry_time TEXT,
    exit_time TEXT,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES Student(student_id)
)
''')

# 3️⃣ Medical Info Table
c.execute('''
CREATE TABLE IF NOT EXISTS MedicalInfo(
    student_id INTEGER PRIMARY KEY,
    blood_group TEXT,
    allergies TEXT,
    medical_conditions TEXT,
    emergency_contact TEXT,
    FOREIGN KEY(student_id) REFERENCES Student(student_id)
)
''')

# 4️⃣ Leave Request Table
c.execute('''
CREATE TABLE IF NOT EXISTS LeaveRequest(
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    from_date TEXT,
    to_date TEXT,
    reason TEXT,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY(student_id) REFERENCES Student(student_id)
)
''')

conn.commit()
conn.close()

print("✅ Database and tables created successfully!")
