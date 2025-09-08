"""
Input:

Line 1: integer n
Line 2: n space-separated integers
Output: Print count of: positive numbers, negative numbers, zeros

"""
list = []
num = int(input("enter the number: "))
for i in range(num):
    list.append(int(input()))

counter_pos = 0
counter_neg = 0
counter_zer = 0
print(list)
for i in list:
    if i > 0:
        counter_pos += 1
    elif i < 0:
        counter_neg += 1
    else:
        counter_zer += 1

print(f"Postive: {counter_pos}\nNegtive: {counter_neg}\nZero: {counter_zer}")