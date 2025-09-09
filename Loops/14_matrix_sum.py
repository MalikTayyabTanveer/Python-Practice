"""
Input:
Line 1: Two integers rows and cols
Next 'rows' lines: 'cols' space-separated integers each
Output: Sum of all elements in the matrix
"""

#first and working solution
"""MatrixSize = list(map(int, input().split()))
print(len(MatrixSize))

Matrix = []
sum = 0
if len(MatrixSize) == 2:
    for num in range(MatrixSize[0]):
        row = []
        for j in range(MatrixSize[1]):
            num = int(input())
            row.append(num)
            sum += num
        Matrix.append(row)

        print()
        
#Matrix printing
    for row in range(MatrixSize[0]):
        for element in range(MatrixSize[1]):
            print(Matrix[row][element], end=" ")
        print()

#printing the sum
    print(f"Sum : {sum}")"""

#second and efficient solution

row, col = map(int, input().split())

matrix = []
sum = 0

for i in range(row):
    row_value = list(map(int, input().split()))
    if len(row_value) != col:
        print(f"you row {i+1} is exceded the total col i.e. {col}")
    
    matrix.append(row_value)

    for value in row_value:
        sum += value

#Matrix printing
for row in range(row):
    for element in range(col):
        print(matrix[row][element], end=" ")
    print()

#printing the sum
print(f"Sum : {sum}")