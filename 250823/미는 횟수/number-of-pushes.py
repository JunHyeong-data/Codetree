A = input()
B = input()

ans = -1

for i in range(len(A)):
    if A == B:
        ans = i
        break
    
    # 문자열을 오른쪽으로 한 칸씩 밀기
    last_char = A[-1]
    A = last_char + A[:-1]

print(ans)