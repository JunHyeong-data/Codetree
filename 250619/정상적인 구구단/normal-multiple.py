N = int(input())

for i in range(1, N + 1):  # 1단부터 N단까지
    line_results = []
    for j in range(1, N + 1):  # 각 단의 1부터 N까지 곱셈
        line_results.append(f"{i} * {j} = {i * j}")
    print(", ".join(line_results)) # 각 단의 결과를 ', '로 연결하여 한 줄에 출력