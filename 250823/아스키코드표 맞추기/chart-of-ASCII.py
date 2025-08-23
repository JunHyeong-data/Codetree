# 5개의 자연수를 입력받아 정수 리스트로 변환
numbers = list(map(int, input().split()))

# 각 숫자를 아스키 코드 문자로 변환
result_chars = []
for num in numbers:
    result_chars.append(chr(num))

# 변환된 문자들을 공백으로 구분하여 출력
print(*result_chars)