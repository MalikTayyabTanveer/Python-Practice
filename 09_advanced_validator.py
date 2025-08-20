"""Input:
Line 1: A string (username)
Line 2: A number (age)
Line 3: A string (email)
Output: "VALID" if all conditions met, otherwise first failed condition:
Username: 3-15 characters, only letters/numbers
Age: 13-99
Email: contains exactly one '@' and at least one '.'
"""

name = input("Enter your name: ")
age = (input("Enter your age: "))
email = input("Enter your email: ")

if not (3 <= len(name) <= 15 and name.isalnum()):
    print("Not a valid username")
elif not age.isdecimal() or not(13 <= int(age) <= 99):
    print("Not in Valid age")
elif  not email.count("@") == 1 and not email.count(".") >= 1:
    print("email is not correct")
else:
    print("valid")