# n 입력받기
n = int(input())

# 모든 문자열을 합칠 빈 문자열 초기화
result = ""

# n번 반복하여 문자열 입력받고 합치기
for _ in range(n):
    result += input()

# 결과 출력
print(result)