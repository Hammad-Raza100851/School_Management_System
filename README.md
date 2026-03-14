# School_Management_System
A simple School Management System built with Python that manages student and teacher information using JSON files. It allows administrators to add, view, and remove students, while principals can manage teacher details and salaries through a command-line interface.


--->Features
Student System

View student information

Add new student (Admin only)

Remove student (Admin only)

View subjects of each class

Teacher System

View teacher information

Add teacher (Principal only)

Remove teacher (Principal only)

Change teacher salary (Principal only)

Authentication

Two levels of authentication are used:

Role	Access

Admin	Manage students

Principal	Manage teachers and salaries

--->Technologies Used

Python

JSON (for database storage)

Command Line Interface (CLI)

--->Example 

Data Structure

Student File
{
  "ics_1st": {
    "subject": ["english","math","physics","computer"],
    "students_info": {
      "1": {
        "name": "Ali",
        "father_name": "Raza"
      }
    }
  }
}
Teacher File
{
  "math": {
    "teacher_name": "sir_arshad",
    "salary": 150000
  }
}

--->How to Run

Clone the repository

git clone https://github.com/Hammad-Raza100851/school-management-system.git

Open the project folder

Run the program

python run.py

--->Future Improvements

Student marks system

Attendance system

Graphical User Interface (GUI)

Web version using Django

Database integration (MySQL)

--->Author

Developed by Hammad Raza
