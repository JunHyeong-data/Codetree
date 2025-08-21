# 문자열과 찾을 문자를 입력받아 분리
word, target_char = input().split()

# find() 메서드를 이용해 위치 찾기
index = word.find(target_char)

# 결과 출력
if index == -1:
    print("No")
else:
    print(index)