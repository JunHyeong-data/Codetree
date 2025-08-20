# 문자열과 정수 입력 받기
s = input()
k = int(input())

# 문자열을 뒤집기
reversed_s = s[::-1]

# 뒤집은 문자열의 앞에서부터 k개 출력
result = reversed_s[:k]

# 결과 출력
print(result)