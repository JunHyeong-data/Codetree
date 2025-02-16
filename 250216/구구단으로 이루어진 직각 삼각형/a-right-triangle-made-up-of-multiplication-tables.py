n = int(input())

for i in range(1, n+1): #1부터 n까지
    for j in range(1, n - i + 2):#j는 1부터 n까지 i 증가할수록 1씩줄어듬
        if n - i + 1 == j:
            print(f"{i} * {j} = {i * j}", end='\n')
        else:
            print(f"{i} * {j} = {i * j} /", end=' ')
