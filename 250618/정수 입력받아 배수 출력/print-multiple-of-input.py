# 자연수 N을 입력받습니다.
N = int(input())

# N보다 크거나 같은 N의 배수 중 작은 수 5개를 차례로 출력합니다.
# N은 자연수이므로, 첫 번째 배수는 N*1이 됩니다.
# 5개의 배수를 출력해야 하므로, 1부터 5까지 반복합니다.
for i in range(1, 6):
    print(N * i, end=' ')