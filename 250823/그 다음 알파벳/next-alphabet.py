# 문자 입력받기
char = input()

# 'z'인 경우 'a'를 출력
if char == 'z':
    print('a')
else:
    # 문자를 아스키 코드로 변환 후 1을 더하고 다시 문자로 변환
    next_char_code = ord(char) + 1
    next_char = chr(next_char_code)
    print(next_char)