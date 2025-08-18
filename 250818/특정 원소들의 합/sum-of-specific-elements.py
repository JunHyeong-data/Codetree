arr = [list(map(int, input().split())) for _ in range(4)]
tot = []
for i in range(4):
    row_sum = 0
    for j in range(i+1):
        row_sum += arr[i][j]
    tot.append(row_sum)

print(sum(tot))
        