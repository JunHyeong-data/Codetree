# 두 자연수 A, B를 공백으로 구분하여 입력받습니다.
A, B = map(int, input().split())

# B부터 시작하여 A까지 1씩 감소하도록 숫자를 출력합니다.
# range(start, stop, step)에서 stop은 포함되지 않고, step은 감소를 위해 -1로 설정합니다.
# A까지 포함해야 하므로 A-1까지 반복합니다.
for i in range(B, A - 1, -1):
    print(i, end=' ')