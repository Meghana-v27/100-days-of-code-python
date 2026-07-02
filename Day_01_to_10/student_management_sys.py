def display_student(stud_id,name):
    print("Student Details:")
    print(f'Student ID: {stud_id}')
    print(f'Student Name: {name}')
def calculate_total(marks):
    total=0
    for i in marks:
        total+=i
    print(f'Total Marks: {total}')
def calculate_percentage(marks):
    total=0
    for i in marks:
        total+=i
    percentage=(total/5)
    print(f'Percentage: {percentage}%')
def find_grade(percentage):
    if percentage>=90:
        print('Grade: A')
    elif percentage>=75:
        print('Grade: B')
    elif percentage>=60:
        print('Grade: C')
    elif percentage>=40:
        print('Grade: D')
    else:
        print('Grade:Fail')
def highest_mark(marks):
    highest=marks[0]
    for mark in marks:
        if mark>highest:
            highest=mark
    print(f'Highest Mark: {highest}')
def lowest_mark(marks):
    lower=marks[0]
    for mark in marks:
        if mark<lower:
            lower=mark
    print(f'Lowest Mark: {lower}')
def pass_fail(marks):
    for mark in marks:
        if mark<35:
            print("Result: Fail")
            return
    print("Result: Pass")
#student management system
def student_management():
    stud_id=int(input("Enter student id:"))
    stu_name=input("Enter student name:")
    mark1=int(input(f"Enter subject 1 Marks:"))
    mark2=int(input(f"Enter subject 2 Marks:"))
    mark3=int(input(f"Enter subject 3 Marks:"))
    mark4=int(input(f"Enter subject 4 Marks:"))
    mark5=int(input(f"Enter subject 5 Marks:"))
    marks=[mark1,mark2,mark3,mark4,mark5]    
    display_student(stud_id,stu_name)
    calculate_total(marks)
    calculate_percentage(marks)
    total=mark1+mark2+mark3+mark4+mark5
    percentage=(total/5)
    find_grade(percentage)
    highest_mark(marks)
    lowest_mark(marks)
    pass_fail(marks)
student_management()