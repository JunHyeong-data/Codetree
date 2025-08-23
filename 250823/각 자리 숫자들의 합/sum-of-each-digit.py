# 정수 n을 문자열로 입력받기
n_str = input()

# 합계를 저장할 변수 초기화
total_sum = 0

# 문자열의 각 문자를 순회하며 숫자로 변환하여 합산
for digit in n_str:
    total_sum += int(digit)

# 결과 출력
print(total_sum)