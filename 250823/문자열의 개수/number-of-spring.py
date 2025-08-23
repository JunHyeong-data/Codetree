strings = []
while True:
    s = input()
    if s == '0':
        break
    strings.append(s)

# 총 문자열 개수 출력
print(len(strings))

# 홀수 번째 문자열만 출력
for i in range(0, len(strings), 2):
    print(strings[i])