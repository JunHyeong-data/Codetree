# 문자열에서 숫자만 추출하는 함수
def extract_numbers(s):
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
    return int(num_str)

# 두 문자열 입력받기
s1 = input()
s2 = input()

# 각 문자열에서 숫자만 추출하여 정수로 변환
num1 = extract_numbers(s1)
num2 = extract_numbers(s2)

# 두 정수의 합을 출력
print(num1 + num2)