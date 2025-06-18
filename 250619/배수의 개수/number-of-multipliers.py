# 두 정수 A, B를 공백으로 구분하여 입력받습니다.
A, B = map(int, input().split())

# 합을 저장할 변수를 초기화합니다.
total_sum = 0

# A부터 B까지 반복하며 홀수의 합을 구합니다.
for i in range(A, B + 1):
    if i % 2 != 0:  # i가 홀수이면
        total_sum += i

# 홀수의 합을 출력합니다.
print(total_sum)