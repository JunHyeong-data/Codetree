# 문자열에서 정수 부분만 추출하는 함수
def extract_number(s):
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            break
    return int(num_str)

# 두 문자열 입력받기
s1, s2 = input().split()

# 각 문자열에서 정수 부분 추출하여 합산
num1 = extract_number(s1)
num2 = extract_number(s2)
total_sum = num1 + num2

# 결과 출력
print(total_sum)