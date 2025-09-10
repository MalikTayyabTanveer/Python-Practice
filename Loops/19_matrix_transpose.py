"""
Input:

Line 1: Two integers rows and cols
Next 'rows' lines: 'cols' space-separated integers each
Output: Transposed matrix (swap rows and columns)
"""

row, col = map(int, input().split())

#intializing the matrix
matrix = []
for _ in range(row):

    values = list(map(int, input().split()))

    if len(values) != col:
        print("value entered more than column")
        exit()
    matrix.append(values)

#initializing the transpose matrix
transmat = []
for _ in range(col):
    transmat.append([0]*row)

#converting the matrix into transpose
for i in range(row):
    for j in range(col):
        transmat[j][i] = matrix[i][j]

    print()

for ro in (transmat):
    for ele in ro:
        print(ele, end=" ")
    print()
