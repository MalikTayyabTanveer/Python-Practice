"""Input: Two values (any type) and a comparison operator (==, !=, <, >, <=, >=)
Output: Result of comparison or "INVALID" if comparison not possible"""

one = input("Enter first value: ")
second = input("Enter second value: ")
op= input("Enter comparison operator: ")

try:
    float1 = float(one)
    float2 = float(second)

    try:
        match op:
            case "==":
                print(float1 == float2)
            case "!=":
                print(float1 != float2)
            case "<":
                print(float1 < float2)
            case ">":
                print(float1 > float2)
            case "<=":
                print(float1 <= float2)
            case ">=":
                print(float1 >= float2)
            case _:
                raise ValueError("Invalid operator")
    except ValueError as e:
        print(f"error: {e}")

except ValueError:
    try:
        match op:
            case "==":
                print(one == second)
            case "!=":
                print(one != second)
            case "<":
                print(one < second)
            case ">":
                print(one > second)
            case "<=":
                print(one <= second)
            case ">=":
                print(one >= second)
            case _:
                raise ValueError("Invalid operator")
    except ValueError as e:
        print(f"error: {e}")