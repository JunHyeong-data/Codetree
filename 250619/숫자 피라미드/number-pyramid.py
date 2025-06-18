N = int(input())

for i in range(1, N + 1): # i는 1부터 N까지
    # i를 i번 반복하여 리스트를 만들고, ' '로 연결하여 출력
    print(' '.join([str(i) for _ in range(i)]))