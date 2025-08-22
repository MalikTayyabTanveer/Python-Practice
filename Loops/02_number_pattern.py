"""Input: One integer n (1 ≤ n ≤ 10)
Output: Print numbers from 1 to n, each on separate line, then print their sum"""

num = int(input("Enter the numberL(1 to 10): "))
sum = 0
if 1 <= num <= 10:
    for n in range(1, num+1):
        print(n)
        sum += n
    print(f"Sum: {sum}")
else:
    print("enter the number in given range.")
