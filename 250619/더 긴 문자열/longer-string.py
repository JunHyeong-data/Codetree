# 두 개의 단어를 공백을 사이에 두고 입력받습니다.
word1, word2 = input().split()

# 각 단어의 길이를 계산합니다.
len_word1 = len(word1)
len_word2 = len(word2)

# 두 단어의 길이를 비교하여 더 긴 단어와 그 길이를 출력합니다.
if len_word1 > len_word2:
    print(word1, len_word1)
elif len_word2 > len_word1:
    print(word2, len_word2)
else: # 두 단어의 길이가 같을 경우
    print("same")