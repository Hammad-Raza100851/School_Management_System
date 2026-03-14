from main import SMS

s = SMS()
print("--------------------------- WELCOME TO AGSC ---------------------------")
choice1 = input("Enter 'student' for student system or Enter 'teacher' for teacher sytem : ")
if choice1 == 'student' :
    x = True
    while x :
        choice2 = input('''
        Enter '1' for Student Information
        Enter '2' for Add Student (Admin only)
        Enter '3' for Remove Student (Admin only) 
        Enter '4' to Quit  : 
          ''')
        if choice2 == '1' :
            s.student_info()
        elif choice2 == '2' : 
            s.add_student()
        elif choice2 == '3' :
            s.remove_student()
        elif choice2 == '4' :
            x = False
        else :
            print("Wrong Choice..")
elif choice1 == 'teacher' : 
    x = True 
    while x :
        choice3 = input('''
        Enter '1' for Teacher Information
        Enter '2' for Add Teacher (Principal only)
        Enter '3' for Remove Teacher (Principal only)
        Enter '4' for Change Teacher Salary (Principal only)
        Enter '5' to Quit  :                 
            ''')
        if choice3 == '1' :
            s.teacher_info()
        elif choice3 == '2' : 
            s.add_teacher()
        elif choice3 == '3' :
            s.remove_teacher()
        elif choice3 == '4':
            s.change_salary()
        elif choice3 == '5' :
            x = False
        else :
            print("Wrong Choice..")
else : 
    print("Wrong Choice..")