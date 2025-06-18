# 두 자연수 A, B를 공백으로 구분하여 입력받습니다.
A, B = map(int, input().split())

# 짝수의 합을 저장할 변수를 초기화합니다.
sum_of_evens = 0

# A부터 B까지 반복하며 짝수를 찾아 합산합니다.
for i in range(A, B + 1):
    if i % 2 == 0:  # i가 짝수이면
        sum_of_evens += i

# 짝수의 합을 출력합니다.
print(sum_of_evens)