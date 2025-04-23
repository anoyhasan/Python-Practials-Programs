A = [[1, 5, 8], [4, 6, 7], [7, 2, 3]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i] = A[i][j]

for t in result:
    print(t)