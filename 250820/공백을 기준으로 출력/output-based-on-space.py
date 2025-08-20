# 두 줄 입력 받기
line1 = input()
line2 = input()

# 두 문자열 합치기
combined_string = line1 + line2

# 공백이 제거된 문자열을 저장할 변수 초기화
result_string = ''

# 합쳐진 문자열을 하나씩 반복하면서 확인
for char in combined_string:
    if char != ' ':  # 공백이 아니면
        result_string += char # 새 문자열에 추가

# 결과 출력
print(result_string)