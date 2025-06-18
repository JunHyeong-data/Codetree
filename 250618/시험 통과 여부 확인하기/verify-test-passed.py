# 점수 N을 입력받습니다.
N = int(input())

# N이 80점 이상이면 "pass"를 출력합니다.
if N >= 80:
    print("pass")
# 그렇지 않다면, 80점에서 N을 뺀 값만큼 "more score"를 출력합니다.
else:
    needed_score = 80 - N
    print(f"{needed_score} more score")