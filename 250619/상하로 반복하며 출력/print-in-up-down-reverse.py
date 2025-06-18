N = int(input())

for r in range(1, N + 1): # 각 행 (1부터 N까지)
    line_str = "" # 각 줄의 문자열을 여기에 저장
    for c in range(1, N + 1): # 각 열 (1부터 N까지)
        if c % 2 == 1: # 홀수 번째 열
            line_str += str(r)
        else: # 짝수 번째 열
            line_str += str(N - r + 1)
    print(line_str) # 완성된 줄 문자열 출력