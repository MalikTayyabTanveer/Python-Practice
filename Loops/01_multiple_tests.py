"""
Input:

First line: number of test cases t
Next t lines: one integer per line
Output: For each test case, print "EVEN" or "ODD"""

TestCaseNumber = int(input("Enter the number of test cases: "))
list = []
for num in range(TestCaseNumber):
    list.append(int(input()))

for num in list:
    if num % 2 == 0:
        print("Even")
    else:
        print("ODD")