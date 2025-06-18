N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    total_sum = 0
    for num in range(a, b + 1): # a부터 b까지 반복
        if num % 2 == 0: # 짝수인지 확인
            total_sum += num
    print(total_sum)