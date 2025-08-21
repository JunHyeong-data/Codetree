s = input()

s_list = list(s) # 문자열을 리스트로 변환

first_char = s[0]
second_char = s[1]

for i in range(len(s_list)):
    if s_list[i] == first_char:
        s_list[i] = second_char
    elif s_list[i] == second_char:
        s_list[i] = first_char
        
print("".join(s_list))