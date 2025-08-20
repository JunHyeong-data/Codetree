# 10개의 문자열을 저장할 리스트
words = []
for _ in range(10):
    words.append(input())

# 마지막에 찾을 문자 입력
target_char = input()

# 조건에 맞는 문자열이 있었는지 추적하는 변수
found_any = False

# 문자열을 순회하며 마지막 문자를 직접 확인하고 출력
for word in words:
    if word[-1] == target_char:
        print(word)
        found_any = True

# 조건에 맞는 문자열이 없었을 경우 'None' 출력
if not found_any:
    print('None')