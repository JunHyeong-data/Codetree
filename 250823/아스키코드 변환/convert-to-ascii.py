# 영문자 a와 정수 b를 입력받아 변수에 저장
a, b = input().split()
b = int(b)

# ord() 함수로 문자를 아스키 코드로 변환
result_a = ord(a)

# chr() 함수로 정수를 아스키 문자로 변환
result_b = chr(b)

# 결과를 공백으로 구분하여 출력
print(result_a, result_b)