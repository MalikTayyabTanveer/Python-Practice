"""
Input: One integer n (2 ≤ n ≤ 100)
Output: "PRIME" if n is prime, "NOT PRIME" if not (use loop to check divisibility)
"""
"""
li = []

for no in range(2,101):
    prime = True
    for i in range(2, no):
        if no % i == 0:
            prime = False
    if prime:
        li.append(no)

print(li)
num = int(input("enter the integer: "))
if 2 <= num <= 100:
    while num in li:
        print("Prime")
        break
    else:
        print("Not prime")"""

#second solution

num = int(input("enter the integer: "))
if 2 <= num <= 100:
    prime = True

    for i in range(2 , int(num**0.5)+1):
        if num % i == 0:
            prime = False
    if prime:
        print("prime")
    else:
        print("Not prime")