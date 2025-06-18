# 물의 온도 n을 정수로 입력받습니다.
n = int(input())

# 0℃ 미만일 경우 "ice" 출력
if n < 0:
    print("ice")
# 100℃ 이상일 경우 "vapor" 출력
elif n >= 100:
    print("vapor")
# 그 사이 (0℃ 이상 100℃ 미만)일 경우 "water" 출력
else:
    print("water")