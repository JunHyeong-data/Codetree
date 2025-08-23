# 영문자 두 개 입력받기
char1, char2 = input().split()

# 아스키 코드 값으로 변환
ascii1 = ord(char1)
ascii2 = ord(char2)

# 합과 차 계산
ascii_sum = ascii1 + ascii2
ascii_diff = abs(ascii1 - ascii2) # abs() 함수로 항상 양수값 구하기

# 결과 출력
print(ascii_sum, ascii_diff)