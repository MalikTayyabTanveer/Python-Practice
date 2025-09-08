"""
Input: Keep reading integers until user enters -1
Output: For each number (except -1), print if it's "HIGH" (>50), "MEDIUM" (10-50), or "LOW" (<10)

"""
num = 0
list = []
while num != -1:
    num = int(input("input = "))
    if num != -1:
        list.append(num)

for nums in list:
    if nums > 50:
        print("High")
    elif 10 <= nums <= 50:
        print("Meduim")
    else:
        print("Low")
