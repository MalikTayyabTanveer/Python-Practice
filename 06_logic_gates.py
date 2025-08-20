print(True and False)
try:
    str1 = input("enter the first bool value: ")
    str2 = input("enter the second bool value: ")
    op = input("enter the bool operation: ").lower()

    if str1.upper() == "TRUE":
        str1 = True
    elif str1.upper() == "FALSE":
        str1 = False
    else:
       raise ValueError("Invalid boolean value entered.")

    if str2.upper() == "TRUE":
        str2 = True
    elif str2.upper() == "FALSE":
        str2 = False
    else:
        raise ValueError("Invalid boolean value entered.")

    match op:
        case "and":
            print(str1 and str2)
        case "or":
            print(str1 or str2)
        case "xor":
            print(str1 ^ str2)
        case _:
            raise ValueError("Invalid operation entered.")
except ValueError as e:
    print(f"Error : {e}")