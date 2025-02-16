n = int(input())

for i in range(1, n+1): # 1부터 n까지
    for j in range(1, n+1): #1부터 n까지
        if (i + j) % 4 == 0:
            print(f"({i}, {j})", end='\n')
        else:
            print(f"({i}, {j})", end=' ')