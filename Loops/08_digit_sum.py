"""
Input: One positive integer
Output: Sum of all its digits using a loop (don't use built-in sum)
"""

num = (input(""))
sum = 0
for i in num:
    sum += int(i)
print(sum)