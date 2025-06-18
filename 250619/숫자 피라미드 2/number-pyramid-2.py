N = int(input())

current_num = 1
for i in range(1, N + 1): # i는 현재 줄에 출력할 숫자의 개수 (1부터 N까지)
    line_numbers = []
    for _ in range(i): # i번 반복하여 i개의 숫자 생성
        line_numbers.append(str(current_num))
        current_num += 1
    print(" ".join(line_numbers))