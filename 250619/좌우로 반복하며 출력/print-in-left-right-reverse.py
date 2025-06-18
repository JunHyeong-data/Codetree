N = int(input())

for r in range(N): # N개의 줄
    line_numbers = []
    if r % 2 == 0: # 짝수 번째 줄 (0, 2, ...) - 오름차순
        for c in range(1, N + 1):
            line_numbers.append(str(c))
    else: # 홀수 번째 줄 (1, 3, ...) - 내림차순
        for c in range(N, 0, -1):
            line_numbers.append(str(c))
    print("".join(line_numbers))