start, end = map(int, input().split())
nt = 0
# Write your code here!
for i in range(start, end+1): #start부터 end까지 반복
    cnt = 0 #초기화
    for j in range(1, i+1): #1부터 i까지 반복
        if i % j == 0: #약수인지 확인
            cnt += 1 #약수이면 0에더하기
    if cnt == 3:
        nt += 1
print(nt)