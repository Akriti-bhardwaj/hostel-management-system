Hostel Management System

The Hostel Management System is a web-based application developed using Python, SQLite, and Streamlit.
It is designed to provide an efficient, centralized platform for managing hostel operations, including student records, entry and exit tracking, medical information maintenance, leave request processing, and analytical reporting.
The system supports automated demo data population to facilitate testing and demonstration without manual data entry.

1. Key Features
1.1 Student Information Management

Register and maintain comprehensive student profiles

Record guardian and emergency contact information

Assign and manage room allocations

Search, sort, and filter student records for quick access

1.2 Entry and Exit Monitoring

Log student check-ins and check-outs with timestamps

Maintain complete history of movements for security and auditing

Filter logs based on date, student, or status

1.3 Medical Information Tracking

Store and update blood group, allergies, and medical conditions

Maintain emergency contacts and health-related documentation

Provide quick reference for urgent or medical situations

1.4 Leave Request Workflow

Students can submit leave requests with details and supporting reasons

Administrators can approve or reject requests

Track request history and status trends for reporting

1.5 Analytical Dashboard

Visual insights using charts and metrics

Department-wise and year-wise distribution of students

Leave request statistics and approval trends

Summary indicators for operational overview

2. Technology Stack
Layer	Technology
Frontend Interface	Streamlit
Backend Logic	Python
Database	SQLite
Data Visualization	Plotly and Streamlit built-in charting
3. System Architecture
hostel-management-system/
│
├── app.py              # Main Streamlit web application
├── backend.py          # Functional logic and database operations
├── database.py         # Database schema and initialization
├── hostel.db           # SQLite relational database
├── test_backend.py     # Script used for backend functionality verification
└── README.md           # Project documentation

4. Installation and Usage
4.1 Prerequisites

Python 3.x

pip package manager

Streamlit installed locally

4.2 Setup Instructions
pip install streamlit plotly

4.3 Launching the Application
streamlit run app.py

4.4 Accessing the Interface

Open the browser and navigate to:

http://localhost:8501

5. Demonstration Data

The system automatically generates sample:

Student records

Entry and exit logs

Leave requests with varied statuses

These records ensure the dashboards and analytical components display meaningful data immediately upon deployment.

6. Applications

This project is applicable for:

University and college hostel administration

Residential facility management

Academic project submissions

Demonstrations of database-driven web applications

Prototyping digital record management systems

7. Institution

Chandigarh University

8. License

This project is intended for educational and demonstration purposes.
Users may customize or extend the system as required.
