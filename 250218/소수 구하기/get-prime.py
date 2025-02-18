n = int(input())

for i in range(1, n+1): #n번 반복
    cnt = 0
    for j in range(1, i+1): #1부터 i까지
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i, end=' ')
    