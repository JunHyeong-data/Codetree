# 한 줄에 있는 10개의 문자열을 입력받아 리스트에 저장
words = input().split()

# 총 길이를 저장할 변수 초기화
total_length = 0

# 리스트의 각 단어의 길이를 더함
for word in words:
    total_length += len(word)

# 결과 출력
print(total_length)