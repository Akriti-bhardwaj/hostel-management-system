import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import backend
from datetime import datetime, date, timedelta

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="Hostel Management System", 
    page_icon="🏨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# STYLING
# ------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
* { font-family: 'Poppins', sans-serif; }
h1 { color: #1E293B; font-weight: 700; margin-bottom: 0.5rem; }
h2, h3, h4 { color: #334155; font-weight: 600; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0F172A, #1E293B); }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: #E2E8F0; }
.stButton>button {
    background: linear-gradient(135deg, #3B82F6, #2563EB);
    color: white; border-radius: 10px; padding: 10px 24px; border: none;
    font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(59,130,246,0.3);
}
.stButton>button:hover { background: linear-gradient(135deg, #2563EB, #1D4ED8);
    box-shadow: 0 6px 12px rgba(59,130,246,0.4); transform: translateY(-2px);
}
.metric-card { background: #F8FAFC; border-radius: 16px; padding: 24px; border: 2px solid #E2E8F0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# LOAD DATA HELPER
# ------------------------------
def load_data():
    try:
        students = backend.view_students()
        logs = backend.view_logs()
        leaves = backend.view_leave_requests()

        df_students = pd.DataFrame(students, columns=["ID", "Name", "Dept", "Year", "Contact", "Guardian", "Guardian Contact", "Room"]) if students else pd.DataFrame()
        df_logs = pd.DataFrame(logs, columns=["Log ID", "Student ID", "Entry", "Exit", "Status"]) if logs else pd.DataFrame()
        df_leaves = pd.DataFrame(leaves, columns=["Req ID", "Student ID", "From", "To", "Reason", "Status"]) if leaves else pd.DataFrame()
        return df_students, df_logs, df_leaves
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# ------------------------------
# SIDEBAR
# ------------------------------
st.sidebar.title("🏨 Hostel Portal")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "📋 Navigation",
    ["🏠 Dashboard", "👨‍🎓 Students", "🕓 Entry Logs", "💊 Medical Info", "✈️ Leave Requests", "📊 Analytics"]
)

st.sidebar.markdown("---")
st.sidebar.info("🏫 **Chandigarh University**\n\n📅 " + datetime.now().strftime("%B %d, %Y"))

# ------------------------------
# DASHBOARD
# ------------------------------
if menu == "🏠 Dashboard":
    st.title("🏨 Hostel Management Dashboard")
    st.markdown("### Welcome to Chandigarh University Hostel Management System")

    df_students, df_logs, df_leaves = load_data()
    if df_students.empty:
        st.warning("⚠️ No data available. Please add students.")
        st.stop()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👨‍🎓 Total Students", len(df_students))
    col2.metric("🚪 Total Logs", len(df_logs))
    col3.metric("⏳ Pending Leaves", len(df_leaves[df_leaves["Status"] == "Pending"]) if not df_leaves.empty else 0)
    col4.metric("✅ Approved Leaves", len(df_leaves[df_leaves["Status"] == "Approved"]) if not df_leaves.empty else 0)

    st.markdown("---")

    st.subheader("📊 Visual Insights")
    col1, col2, col3 = st.columns(3)

    if not df_students.empty:
        with col1:
            dept_count = df_students["Dept"].value_counts().reset_index()
            dept_count.columns = ["Department", "Count"]
            fig = px.pie(dept_count, names="Department", values="Count", title="Students by Department", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            year_count = df_students["Year"].value_counts().reset_index()
            year_count.columns = ["Year", "Count"]
            fig2 = px.bar(year_count, x="Year", y="Count", color="Count", title="Students by Year")
            st.plotly_chart(fig2, use_container_width=True)

        with col3:
            if not df_leaves.empty:
                status_count = df_leaves["Status"].value_counts().reset_index()
                status_count.columns = ["Status", "Count"]
                fig3 = go.Figure(data=[go.Bar(
                    x=status_count["Status"],
                    y=status_count["Count"],
                    marker_color=['#10B981', '#F59E0B', '#EF4444']
                )])
                fig3.update_layout(title="Leave Request Status")
                st.plotly_chart(fig3, use_container_width=True)

# ------------------------------
# STUDENTS
# ------------------------------
elif menu == "👨‍🎓 Students":
    st.title("👨‍🎓 Student Management")

    tab1, tab2 = st.tabs(["➕ Add Student", "📋 View Students"])

    with tab1:
        with st.form("add_student_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name")
                dept = st.text_input("Department")
                year = st.number_input("Year", 1, 5)
                contact = st.text_input("Contact Number")
            with col2:
                guardian = st.text_input("Guardian Name")
                guardian_contact = st.text_input("Guardian Contact")
                room = st.text_input("Room Number")
            submit = st.form_submit_button("Add Student")
            if submit:
                backend.add_student(name, dept, year, contact, guardian, guardian_contact, room)
                st.success(f"✅ {name} added successfully!")

    with tab2:
        df_students, _, _ = load_data()
        if not df_students.empty:
            st.dataframe(df_students, use_container_width=True)
        else:
            st.info("No student records found.")

# ------------------------------
# ENTRY LOGS
# ------------------------------
elif menu == "🕓 Entry Logs":
    st.title("🕓 Entry / Exit Logs")
    students = backend.view_students()
    if not students:
        st.warning("⚠️ No students found.")
    else:
        student_dict = {f"{s[1]} (ID {s[0]})": s[0] for s in students}
        choice = st.selectbox("Select Student", list(student_dict.keys()))
        sid = student_dict[choice]

        col1, col2 = st.columns(2)
        if col1.button("✅ Check-In"):
            backend.add_entry(sid)
            st.success("Entry recorded successfully!")
        if col2.button("🚪 Check-Out"):
            backend.add_entry(sid, exit_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            st.success("Exit recorded successfully!")

        _, logs, _ = load_data()
        if not logs.empty:
            st.dataframe(logs, use_container_width=True)

# ------------------------------
# MEDICAL INFO
# ------------------------------
elif menu == "💊 Medical Info":
    st.title("💊 Medical Information")
    students = backend.view_students()
    if students:
        student_dict = {f"{s[1]} (ID {s[0]})": s[0] for s in students}
        choice = st.selectbox("Select Student", list(student_dict.keys()))
        sid = student_dict[choice]

        with st.form("medical_form"):
            blood = st.text_input("Blood Group")
            allergies = st.text_area("Allergies")
            conditions = st.text_area("Medical Conditions")
            emergency = st.text_input("Emergency Contact")
            if st.form_submit_button("Save Info"):
                backend.add_medical_info(sid, blood, allergies, conditions, emergency)
                st.success("Medical info saved successfully!")

# ------------------------------
# LEAVE REQUESTS
# ------------------------------
elif menu == "✈️ Leave Requests":
    st.title("✈️ Leave Management")
    students = backend.view_students()
    if students:
        student_dict = {f"{s[1]} (ID {s[0]})": s[0] for s in students}
        choice = st.selectbox("Select Student", list(student_dict.keys()))
        sid = student_dict[choice]

        with st.form("leave_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            from_date = col1.date_input("From Date", date.today())
            to_date = col2.date_input("To Date", date.today())
            reason = st.text_area("Reason for Leave")
            if st.form_submit_button("Submit Request"):
                backend.add_leave_request(sid, str(from_date), str(to_date), reason)
                st.success("Leave request submitted!")

        _, _, df_leaves = load_data()
        if not df_leaves.empty:
            st.dataframe(df_leaves, use_container_width=True)
        else:
            st.info("No leave requests found.")

# ------------------------------
# ANALYTICS
# ------------------------------
elif menu == "📊 Analytics":
    st.title("📊 Hostel Analytics Dashboard")
    df_students, df_logs, df_leaves = load_data()
    if df_students.empty:
        st.warning("No data available for analytics.")
    else:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Students", len(df_students))
        col2.metric("Logs", len(df_logs))
        col3.metric("Leaves", len(df_leaves))
        col4.metric("Departments", df_students["Dept"].nunique())
        st.markdown("---")
        dept_data = df_students["Dept"].value_counts().reset_index()
        dept_data.columns = ["Department", "Count"]
        fig = px.bar(dept_data, x="Department", y="Count", title="Department Strength")
        st.plotly_chart(fig, use_container_width=True)
