"""
Input: One string
Output: For each character with its position (use enumerate), print: "Position X: character """


string = input("enter the string: ")

for idx, char in enumerate(string):
    print(f"Position {idx}: {char}")
    