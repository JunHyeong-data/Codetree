n = int(input())

for i in range(n, 0, -1):  # n부터 1까지 감소시키며 반복
    for j in range(i, n + 1):  # i부터 n까지 증가시키며 출력
        print(j, end=" ")
    print()  # 줄바꿈
