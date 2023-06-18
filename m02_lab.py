# Ryder Meehan
# m02_lab.py
# name: string for a student's name
# gpa: float for a student's GPA
# This program takes a student's name as an input and asks the user to
# enter the student's GPA and then outputs if the student has made the
# honor roll or dean's list

name = str

while name != "ZZZ":

    name = input("Enter student name or ZZZ to quit: ")

    if name == "ZZZ":
        quit

    else:
        gpa = float(input("Enter student GPA: "))

        if gpa >= 3.5:
            print("Student has made the Dean's List")
        elif gpa >= 3.25:
            print("Student has made the Honor Roll")
        else:
            print("Student is not on the Honor Roll or the Dean's List")
