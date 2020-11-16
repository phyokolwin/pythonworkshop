
m = [[1,2,3],[4,5,6]]
print(m[1][1])

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j])

for row in m:
    for col in row:
        print(col)
