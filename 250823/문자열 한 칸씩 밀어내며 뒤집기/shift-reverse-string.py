input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

s_list = list(input_str)

for query in queries:
    # 요청 1: 가장 앞 문자를 맨 뒤로 옮기기
    if query == 1:
        # 리스트의 맨 앞 요소를 꺼내고
        first_char = s_list.pop(0)
        # 맨 뒤에 추가합니다.
        s_list.append(first_char)
    
    # 요청 2: 가장 뒤 문자를 맨 앞으로 옮기기
    elif query == 2:
        # 리스트의 맨 뒤 요소를 꺼내고
        last_char = s_list.pop()
        # 맨 앞에 삽입합니다.
        s_list.insert(0, last_char)
    
    # 요청 3: 문자열 뒤집기
    elif query == 3:
        # 리스트의 순서를 뒤집습니다.
        s_list.reverse()
    
    # 변경된 리스트를 다시 문자열로 합쳐서 출력합니다.
    print("".join(s_list))