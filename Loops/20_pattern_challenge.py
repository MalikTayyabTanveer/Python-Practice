"""
Input: One integer n (1 ≤ n ≤ 10)
Output: Print hollow square pattern with stars

"""

num = int(input("enter the number: "))

for i in range(num):
    for j in range(num):
        if i == 0 or i == num-1:
            print("*", end="")
        elif j == 0 or j == num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()