# 🏫 School Management System

A simple **School Management System** built with **Python** that manages student and teacher information using **JSON files**.  
It allows administrators to add, view, and remove students, while principals can manage teacher details and salaries through a **command-line interface (CLI)**.

---

## 🚀 Features

### 👩‍🎓 Student System
- 📖 View student information  
- ➕ Add new student (**Admin only**)  
- ❌ Remove student (**Admin only**)  
- 📚 View subjects of each class  

### 👨‍🏫 Teacher System
- 📖 View teacher information  
- ➕ Add teacher (**Principal only**)  
- ❌ Remove teacher (**Principal only**)  
- 💰 Change teacher salary (**Principal only**)  

### 🔐 Authentication
Two levels of authentication are used:

| Role       | Access                           |
|-----------|----------------------------------|
| 🛡️ Admin      | Manage students                 |
| 👑 Principal | Manage teachers and salaries    |

---

## 🛠️ Technologies Used
- 🐍 **Python**  
- 💾 **JSON** (for database storage)  
- 🖥️ **Command Line Interface (CLI)**  

---

## 📂 Example Data Structure

### Student File
```json
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
