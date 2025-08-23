# 두 정수 입력받기
a, b = map(int, input().split())

# 두 정수의 합 구하기
total_sum = a + b

# 합을 문자열로 변환
sum_str = str(total_sum)

# 문자열에서 '1'의 개수 세기
count_one = sum_str.count('1')

# 결과 출력
print(count_one)