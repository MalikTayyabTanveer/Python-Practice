"""
 Input: One integer n (1 ≤ n ≤ 10)
Output: Print n×n multiplication table in grid format 
"""
num = int(input("enter the number: "))

for i in range(1, num+1):
    for j in range(1, num+1):
        print(i*j, end=" ")
    print()
