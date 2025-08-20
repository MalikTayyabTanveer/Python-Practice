"""Input: A value and target type (int/float/str/bool)
Output: Converted value or "IMPOSSIBLE" if conversion fails"""

value = input("Enter the value: ").strip().lower()
T_type = input("Enter the target type: ").lower()

try:
    if value == "true":
            value = True
    elif value == "false":
            value = False
    else:
        value = float(value)

    match T_type:
        case "int":
            print(int(value))
        case "float":
            print(float(value))
        case "bool":
            print(bool(value))
        case "str":
            print(str(value))
        case _:
            print("IMPOSSIBLE")

except (ValueError, TypeError):
    if T_type == "str":
         print(value)
    elif T_type == "bool":
         print(bool(value))
    else:
         print("IMPOSSIBLE")