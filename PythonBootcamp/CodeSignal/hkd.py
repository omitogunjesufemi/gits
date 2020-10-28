matrix = [[1, 0, 5, 12],
          [0, 8, 0, 0],
          [-6, 7, 11, 19]]

row = len(matrix)
column = len(matrix[0])
sum = 0
for i in range(column):
    for j in range(row):
        cell = matrix[j][i]
        if cell == 0:
            break
        else:
            sum += cell
print(sum)
