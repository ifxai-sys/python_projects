students=[]
def add_Student():
    Name=input("Enter the name of student:")
    Age=int(input("Enter the age :"))
    Subjects=[]
    print("Enter 4 subjects you enrolled.")
    for i in range(4):
       Subject= input(f"Enter subject {i+1} :")
       Subjects.append(Subject)
    grade_input=input("enter the grades for respective subjects.(seperated by commas)")   
    grade=[int(i.strip())for i in grade_input.split(",")]
    student=(Name,Age,Subjects,grade)
    students.append(student)
    print("Student added successfully")

def view_students():
    if not students:
        print("No student enrolled .")
        return
    print("--------Student record--------")
    for i , student in enumerate(students,start=1):
        Name,Age,Subjects,grade=student
        print(f"{i}. Name: {Name} | Age: {Age}")
        for j in range (4):
            print(f" {j+1}. Subject={Subjects[j]} | Grade={grade[j]}")
        print()

def search_student():
    if not students:
        print("No student enrolled .")
        return  
    
    search_name=input("Enter the name of student:")
    found=False

    for i, student in enumerate(students, start=1):
        Name,Age,Subjects,grade=student
        if Name.lower() == search_name.lower():
          print(f"{i}. Name: {Name} | Age: {Age}")
          for j in range(4):
            print(f" {j+1}. Subject={Subjects[j]} |Grade={grade[j]}")
          found=True
          break    
    if not found:
       print("Student not found.")  

def top_performer():
    if not students:
        print("No student enrolled .")
        return
    
    highest_grade=0
    top_student=None  

    for student in students:
        Name,Age,Subjects,grade=student
        avg=sum(grade) / len(grade)
        if avg>highest_grade:
            highest_grade=avg
            top_student=student

    if top_student:
        Name, Age, Subjects, grade = top_student
        print(f"Name: {Name} | Age: {Age} | Average Grade: {highest_grade:.2f}")
        for i in range(4):
            print(f" {i+1}. Subject: {Subjects[i]} | Grade:{grade[i]}")
def menu():

    print("\n====== Student Management Menu ======")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by name")
    print("4. Show top performer")
    print("5. Exit")

    option = input("Select option from menu: ")

    match option:
        case "1":
            add_Student()
        case "2":
            view_students()
        case "3":
            search_student()
        case "4":
            top_performer()
        case "5":
            print("Exiting... Goodbye!")
            exit()
        case _:
            print("❌ Invalid option. Try again.")
            menu() 
while True:
    menu()

      








