# 문자열 A와 B를 입력받기
A, B = input().split()

# AB 문자열과 BA 문자열 만들기
AB = A + B
BA = B + A

# 두 문자열을 정수로 변환하여 합산
total_sum = int(AB) + int(BA)

# 결과 출력
print(total_sum)