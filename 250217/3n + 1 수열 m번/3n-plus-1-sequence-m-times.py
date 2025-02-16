m = int(input())

for _ in range(m):
    n = int(input())
    cnt = 0

    while n != 1:  # n이 1이 될 때까지 계속 반복
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1

    print(cnt)
