"""
Input:
Line 1: Two integers rows and cols
Next 'rows' lines: 'cols' space-separated integers each
Output: Maximum element and its position (row, col) - 0-indexed

"""

row, col = map(int, input().split())

matrix = []

#Inputing the values in matrix
for i in range(row):
    row_value = list(map(int, input().split()))

    if len(row_value) != col:
        print(f"you row {i+1} is exceded the total col i.e. {col}")
    
    matrix.append(row_value)

max = matrix[0][0]
Rloc = 0
Cloc = 0

# finding the max and also the location of max
for rows in range(row):
    for element in range(col):
        if matrix[rows][element] > max:
            max = matrix[rows][element]
            Rloc = rows
            Cloc = element

print(f"Maximum element: {max}")
print(f"Position (row, col): {Rloc} {Cloc}")