input_string_A = input()
commands = input()

s_list = list(input_string_A)

for command in commands:
    # 'L' 명령: 왼쪽으로 한 칸 회전
    if command == 'L':
        # 리스트의 맨 앞 요소를 꺼내서
        first_char = s_list.pop(0)
        # 맨 뒤에 추가합니다.
        s_list.append(first_char)
    
    # 'R' 명령: 오른쪽으로 한 칸 회전
    elif command == 'R':
        # 리스트의 맨 뒤 요소를 꺼내서
        last_char = s_list.pop()
        # 맨 앞에 삽입합니다.
        s_list.insert(0, last_char)

# 모든 명령을 수행한 후, 최종 리스트를 다시 문자열로 합쳐서 출력합니다.
print("".join(s_list))