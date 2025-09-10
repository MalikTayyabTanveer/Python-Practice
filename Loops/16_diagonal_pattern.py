"""

Input: One integer n (1 ≤ n ≤ 10)
Output: Print n×n grid where main diagonal has 1s, others have 0s

"""

num = int(input("enter the number: "))

if 1 <= num <= 10:
    for i in range(num):
        for j in range(num):
            if i == j:
                print(1, end="\t")
            else:
                print(0, end="\t")
        print()