import json

class SMS:
    def __init__(self,student_file="students.json",teacher_file = "teacher.json"):
        self.student_file = student_file
        self.teacher_file = teacher_file
        self.student_dict = self.load_student_file()
        self.teacher_dict = self.load_teacher_file()
    
    def load_student_file(self):
        with open(self.student_file,"r") as bk:
            return json.load(bk)
        
    def save_file(self):
        with open(self.student_file,"w") as bk :
            json.dump(self.student_dict,bk,indent=4)
            
    def admin_authentication(self):
        passs = input("\nenter the admin pass :")
        a = str(1122)
        if passs == a:
            print("Authentication Successful\n")
            return True
        else :
            print("Authentication Unsuccessful")
            return False
        
    def principal_authentication(self) : 
        passs = input("\nenter the principal pass :")
        a = "admin"
        if passs == a:
            print("Authentication Successful\n")
            return True
        else :
            print("Authentication Unsuccessful")
            return False
        
    def student_info(self):
        print("\nics_1st , fcs_1st , ics_2nd , fcs_2nd")
        name = input("enter the class name you want information : ")
        x = self.admin_authentication()
        if x :
            print(f"\nClass : {name} ")
            class_info = self.student_dict.get(name)
            if not class_info: 
                print("Class not found!")
                return
            print(f"Subjects : {class_info.get('subject')}")
            print(f"Roll \tStudents\t Fathers  ")
            for role , info in class_info.get('students_info').items() :
                print(f"{role}\t{info.get('name')}\t\t{info.get('father_name')}")
        else :
            roll = input("Enter your role number : ")
            print(f"\nClass : {name} ")
            class_info = self.student_dict.get(name)
            if not class_info: 
                print("Class not found!")
                return
            info = class_info.get('students_info').get(roll)
            if not info : 
                return
            print(f"Subjects : {class_info.get('subject')}")
            print(f"Roll \tStudents\t Fathers  ")
            print(f"{roll} \t{info.get('name')}\t{info.get('father_name')}")
            
    def add_student(self):
        a = self.admin_authentication()
        if a :
            print("ics_1st , fcs_1st , ics_2nd , fcs_2nd")
            name = input("enter the class name you want add student : ")
            class_info = self.student_dict.get(name)
            if not class_info: 
                print("Class not found!")
                return
            student_name = input("Enter student name: ")
            father_name = input("Enter father name: ")
            role_n = class_info['students_info'].keys()
            role = str(int(max(role_n))+1)
            class_info['students_info'][role]={
                'name' : student_name,
                'father_name' :  father_name
            }
            self.save_file()
            print("Successfuly Added")
        else :
            pass
    
    def remove_student(self):
        a = self.admin_authentication()
        if a :
            print("ics_1st , fcs_1st , ics_2nd , fcs_2nd")
            name = input("enter the class name you want remove student of : ")
            class_info = self.student_dict.get(name)
            if not class_info: 
                print("Class not found!")
                return
            roll = input("enter the roll number of student u wnat to delete : ")
            if roll not in class_info['students_info']:
                print(f"Roll number {roll} not found!")
                return
            ch = input(f"enter 'x' if u want to remove stundent wit rollno {roll} else enter 'y' : ")
            if ch == 'x' :
                del class_info['students_info'][roll]
                print("Successfuly Deleted")
                self.save_file()
            elif ch == 'y' :
                print("You not want to remove student")
            else :
                print("You did not choose eithe 'x' or 'y' ")
            
        else :
            pass            

    def load_teacher_file(self):
        with open(self.teacher_file,"r") as bk:
            return json.load(bk)
        
    def save_teacher_file(self) :
         with open(self.teacher_file,"w") as bk :
            json.dump(self.teacher_dict,bk,indent=6)
            
    def teacher_info(self) :
        print("Principal authentication is u want to see salary otherwise Enter 0 ")
        x = self.principal_authentication()
        if x:
            print("\nSubject : Name , Salary")
            for keys , values in self.teacher_dict.items():
                print(f"{keys} : {values.get('teacher_name')} , {values.get('salary')}")
            
        else:
            print("\nSubject : Name")
            for keys , values in self.teacher_dict.items():
                print(f"{keys} : {values.get('teacher_name')}")
                
    def add_teacher(self):
        x = self.principal_authentication()
        if x :
            name = input("Enter the name of the teacher : ").strip()
            suject = input("Enter the name of his Subject : ").strip()
            salary = input("Enter the salary amount : ")
            self.teacher_dict[suject]={
                "teacher_name" : name ,
                "salary" : salary }
            self.save_teacher_file()
            print("Successfully Added")
            
    def remove_teacher(self):
        a = self.principal_authentication()
        if a :
            subject = input("Enter the name of his Subject : ").strip()
            if subject not in self.teacher_dict:
                print("NO subject Found") 
                return
            name = input("Enter the name of the teacher : ").strip()
            if self.teacher_dict[subject]["teacher_name"] != name:
                print(" No teacher found for this subject")
                return
            ch = input(f"enter 'x' if u want to remove teacher name {name} and subject name{subject} enter 'y' : ")
            if ch == 'x' :
                del self.teacher_dict[subject]
                self.save_teacher_file()
                print("Successfully Deleted ")
            else:
                print("You not want to remove the teacher")
        else:
            pass
        
    def change_salary(self):
            a = self.principal_authentication()
            if a :
                subject = input("Enter the name of his Subject : ").strip()
                if subject not in self.teacher_dict:
                    print("NO subject Found") 
                    return
                name = input("Enter the name of the teacher : ").strip()
                if self.teacher_dict[subject]["teacher_name"] != name:
                    print(" No teacher found for this subject")
                    return
                salary = input("Enter the salary : ")
                ch = input(f"enter 'x' if u want to change salary of teacher : {name} and subject name : {subject} enter 'y' : ")
                if ch == 'x' :
                    self.teacher_dict[subject]['salary'] = salary
                    self.save_teacher_file()
                    print("Successfully Changed ")
                else:
                    print("You not want to salary of the teacher")
            else:
                pass
            