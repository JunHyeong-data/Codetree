arr = [list(map(int, input().split())) for _ in range(2)]
row = []
column = []
for elem in arr:
    row.append(sum(elem) / len(elem))

col_avg = []
for j in range(4):
    col_sum = 0
    for i in range(2):
        col_sum += arr[i][j]
    col_avge = col_sum / 2
    col_avg.append(col_avge)

tot = 0
for i in arr:
    for j in i:
       tot += j         
print(*row)
print(*col_avg)
print(tot / 8)