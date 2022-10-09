matrix= [
    [1,3,6],
    [5,7,9],
    [4,8,5]
]
print(matrix[0][2])
matrix[1][2] = 80
print(matrix[1][2])
print()
for item in matrix:
    for value in item:
        print(value)