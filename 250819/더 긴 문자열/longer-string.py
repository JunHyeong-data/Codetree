# 입력받은 두 단어를 공백으로 나누어 각각 s1, s2에 저장
s1, s2 = input().split()

# 두 단어의 길이를 각각 구함
len1 = len(s1)
len2 = len(s2)

# 길이를 비교하여 조건에 맞게 출력
if len1 > len2:
    print(s1, len1)
elif len2 > len1:
    print(s2, len2)
else:
    print('same')