"""
Input: One integer n (1 ≤ n ≤ 10)
Output: Print triangle where each row has numbers from 1 to row number

"""

num = int(input("enter the number: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()