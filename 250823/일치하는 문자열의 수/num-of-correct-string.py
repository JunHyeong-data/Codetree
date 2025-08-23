# 정수 n과 문자열 A를 입력받기
n, A = input().split()
n = int(n)

# 일치하는 문자열의 개수를 저장할 변수 초기화
count = 0

# n번 반복하며 문자열을 입력받고 A와 일치하는지 확인
for _ in range(n):
    string = input()
    if string == A:
        count += 1

# 결과 출력
print(count)