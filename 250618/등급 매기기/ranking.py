# 점수 N을 입력받습니다.
N = int(input())

# 시험 점수에 따라 등급을 출력합니다.
if N >= 90:
    print("A")
elif N >= 80:
    print("B")
elif N >= 70:
    print("C")
elif N >= 60:
    print("D")
else: # 60점 미만
    print("F")