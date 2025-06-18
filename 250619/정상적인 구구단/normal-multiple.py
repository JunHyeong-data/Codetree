N = int(input())

for i in range(1, N + 1):  # 1단부터 N단까지
    for j in range(1, N + 1):  # 각 단의 1부터 N까지 곱셈
        print(f"{i} * {j} = {i * j}")
    print() # 각 단이 끝날 때마다 빈 줄 출력 (구분선 역할)