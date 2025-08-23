# 문자 입력받기
char = input()

# 'a'인 경우 'z'를 출력
if char == 'a':
    print('z')
else:
    # 문자를 아스키 코드로 변환 후 1을 빼고 다시 문자로 변환
    prev_char_code = ord(char) - 1
    prev_char = chr(prev_char_code)
    print(prev_char)