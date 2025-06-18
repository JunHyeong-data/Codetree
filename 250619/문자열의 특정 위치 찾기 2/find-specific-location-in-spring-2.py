strings = ["apple", "banana", "grape", "blueberry", "orange"]
target_char = input()

matched_strings = []
for s in strings:
    # 세 번째 문자 (인덱스 2) 또는 네 번째 문자 (인덱스 3)가 일치하는 경우
    if (len(s) >= 3 and s[2] == target_char) or \
       (len(s) >= 4 and s[3] == target_char):
        matched_strings.append(s)

# 문제 요구사항에 따라 원본 리스트의 순서대로 출력해야 하므로,
# matched_strings에 추가될 때 이미 순서가 유지됩니다.

for s in matched_strings:
    print(s)
print(len(matched_strings))