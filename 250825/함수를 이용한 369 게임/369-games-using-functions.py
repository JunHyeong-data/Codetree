a, b = map(int, input().split())

# Please write your code here.
def count_369(n):
    s = str(n)  # 숫자를 문자열로 바꿔서
    for digit in s:  # 한 글자씩 확인
        if digit in '369':
            return True

    return False
    
def game(a, b):
    cnt = 0
    for i in range(a, b+1):
        if count_369(i) or i % 3 == 0:
            cnt += 1
    return cnt

print(game(a,b))