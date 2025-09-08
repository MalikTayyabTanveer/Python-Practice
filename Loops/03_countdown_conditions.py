"""Input: Two integers start and end (start > end)
Output: Count from start to end, but skip multiples of 3
"""
start = int(input("start value:"))
end = int(input("en value: "))

while start >= end:
    if start % 3 != 0:
        print(start)
    start -= 1
