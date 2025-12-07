import backend

# 1️⃣ Add new students
backend.add_student("Aarav Sharma", "CSE", 2, "9876543210", "Ramesh Sharma", "9123456789", "A-101")
backend.add_student("Priya Patel", "ECE", 3, "9988776655", "Suresh Patel", "9090909090", "B-202")

# 2️⃣ View students
print("\n📋 All Students:")
for s in backend.view_students():
    print(s)

# 3️⃣ Add entry logs
backend.add_entry(1)  # student ID 1 checks in
backend.add_entry(2)  # student ID 2 checks in

# 4️⃣ View entry logs
print("\n📜 Entry Logs:")
for log in backend.view_logs():
    print(log)

# 5️⃣ Add medical info
backend.add_medical_info(1, "B+", "Peanuts", "Asthma", "9876543210")

# 6️⃣ View medical info
print("\n💊 Medical Info for Student 1:")
print(backend.view_medical_info(1))

# 7️⃣ Add leave requests
backend.add_leave_request(1, "2025-11-13", "2025-11-15", "Going home for Diwali")
backend.add_leave_request(2, "2025-11-20", "2025-11-22", "Medical leave")

# 8️⃣ View leave requests
print("\n📅 All Leave Requests:")
for req in backend.view_leave_requests():
    print(req)

# 9️⃣ Update leave status
backend.update_leave_status(1, "Approved")
backend.update_leave_status(2, "Rejected")

print("\n✅ Updated Leave Requests:")
for req in backend.view_leave_requests():
    print(req)
# 🔟 Update student info
backend.update_student(1, contact="9998887777", room_no="A-201")

print("\n🧾 Updated Student List:")
for s in backend.view_students():
    print(s)

# 1️⃣1️⃣ Delete a student
backend.delete_student(2)

print("\n🗂️ Student List After Deletion:")
for s in backend.view_students():
    print(s)
