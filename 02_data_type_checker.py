"""Write a program that takes any input from user, displays its type, and shows its value in different data types
(if possible). Handle conversion errors gracefully."""

value = input("enter the data: ")


print(f"The initial data type is {type(value)}")

print("\n Conversion to different data type \n")

try:
    int_value = int(value)
    print("As integer: ", value)
except ValueError:
    print("The conversion to int is not possible")

try:
    float_value = float(value)
    print(" As Float: ", value)
except ValueError:
    print("The conversion to float is not possible")

print("Due to the input function, the value always remains string")

