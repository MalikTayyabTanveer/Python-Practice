"""Create a program that stores a student's name, age, and GPA. Display their
information and determine if they're eligible for honors (GPA >= 3.5)."""

name = input("Enter your name : ")
age = int(input("Enter your age : "))
gpa = float(input("Enter your GPA : "))

if gpa >= 3.5:
    print("Congratulation \n Name: {0} \n Age: {1} \n You are Eligible".format(name, age))
else:
    print("You are not eligible")