"""
Input:

Line 1: Integer n (size of array)
Line 2: n space-separated integers
Line 3: Target sum
Output: Count of pairs that sum to target (don't count same element twice)

"""

num = int(input("enter the size of list: "))
value = list(map(int, input().split()))


target = int(input("enter the target value: "))


if len(value) != num:
    print("you exceeded the list range")
    exit()
counter = 0

for i in value:
    for j in value:
        if i < j:
            if i + j == target:
                counter += 1
                print(f"Pairs : {i} + {j} = {target}")

print(f"total count: {counter}")
