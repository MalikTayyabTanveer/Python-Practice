"""
Input: One integer n (1 ≤ n ≤ 5)
Output: Print multiplication table for numbers 1 to n

"""
num = int(input("enter the any number between 1 to 5: "))

if 1 <= num <= 5:
    for i in range(1, 11):
        for j in range(1, num+1):
            print(f"{i} * {j} = {i*j}", end="\t")
        print()