# 한 줄에 있는 10개의 문자열을 입력받아 리스트에 저장
words = input().split()

for i in range(len(words)):
    if i % 2 == 0:
        print(words[i])