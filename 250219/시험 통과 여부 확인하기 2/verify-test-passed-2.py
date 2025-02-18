n = int(input())
cnt = 0
arr = []  # 학생별 점수를 저장할 리스트
sum_val = []  # 총점 저장 리스트
avg = []  # 평균 저장 리스트

for i in range(n):
    scores = list(map(int, input().split()))
    arr.append(scores)  # 리스트에 추가
    sum_val.append(sum(scores))  # 총점 저장
    avg.append(sum_val[i] / 4)  # 평균 저장

for j in range(n):
    if avg[j] >= 60:  # j로 변경
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)
