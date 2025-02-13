n = int(input())
cnt = 1
for i in range(n):
    for j in range(n):
        if i % 2 ==0:
            print(cnt, end=" ")
            cnt+=1
            if j == n - 1 :
                cnt += 1
        else:
            print(cnt, end=" ")
            cnt+=2
            if j == n - 1:
                cnt -= 1
    print()


            


