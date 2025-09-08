""" Input:

Line 1: integer n (number of elements)
Line 2: n space-separated integers
Line 3: target integer to find
Output: Position of first occurrence (0-indexed) or "NOT FOUND

"""

n = int(input("enter the number of integer you want to enter: "))

list = []
for i in range(n):
    list.append(int(input()))

target = int(input("enter the target integer: "))

found = False

for idx, num in enumerate(list):
    if target == num:
        print(f"index: {idx}")
        found = True
        break
    
if not found:
    print("not found")
