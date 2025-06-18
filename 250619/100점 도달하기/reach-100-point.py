# 점수 N을 입력받습니다.
N = int(input())

# 주어진 점수 N부터 100점까지 1점씩 증가하며 각 점수가 어떤 등급에 해당하는지 출력합니다.
for score in range(N, 101):
    if score >= 90:
        print("A", end=' ')
    elif score >= 80:
        print("B", end=' ')
    elif score >= 70:
        print("C", end=' ')
    elif score >= 60:
        print("D", end=' ')
    else: # score < 60
        print("F", end=' ')