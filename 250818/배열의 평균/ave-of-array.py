arr = [list(map(int, input().split())) for _ in range(2)]

row_avg = [sum(row) / len(row) for row in arr]

trans = zip(*arr)
col_avg = [sum(col) / len(col) for col in trans]

tot = 0
for row in arr:
    for num in row:
        tot += num
print(*row_avg)
print(*col_avg)
print(tot/8)    