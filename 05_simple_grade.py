"""Ask for one test score (0-100). Use if-elif-else to assign letter grade 
(A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60). Validate score range."""


try:
    Number = float(input("Enter you grade: "))

    if 90 <= Number <= 100:
        print("Grade A")
    elif 80 <= Number <= 89:
        print("Grade B")
    elif 70 <= Number <= 79:
        print("Grade C")
    elif 60 <= Number <= 69:
        print("Grade D")
    elif 0 <= Number <= 60:
        print("Grade F")
    else:
        print("Enter the Correct value")

except ValueError:
    print("Enter the integer value.")