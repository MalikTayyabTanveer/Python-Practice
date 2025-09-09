""" 
Input: One integer n (1 ≤ n ≤ 10)
Output: Print right triangle pattern with stars
 """

num = int(input("enter the number: "))

for i in range(1, num+1):
    for j in range(i):
        print("*", end="")
    print()
