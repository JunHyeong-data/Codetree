# 한 줄에 있는 10개의 문자열을 입력받아 리스트에 저장
words = input().split()

# 슬라이싱을 이용해 리스트를 역순으로 뒤집기
reversed_words = words[::-1]

# 역순으로 정렬된 리스트의 요소들을 공백으로 구분하여 출력
for rev in reversed_words:
    print(rev)