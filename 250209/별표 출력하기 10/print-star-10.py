n = int(input())
cnt1 = 1
cnt2 = n
for i in range(1,n+1):
    if i % 2 == 1:
        for _ in range(cnt1):
            print('*', end=' ')
        cnt1 += 1
        print()
    else :
        for _ in range(cnt2):
            print('*', end=' ')
        cnt2 -= 1
        print()
cnt2 += 1
cnt1 -= 1
for i in range(n):
    if i % 2 == 1:
        for _ in range(cnt2):
            print('*', end=' ')
        cnt2 += 1
        print()
    else:
        for _ in range(cnt1):
            print('*', end=' ')
        cnt1 -= 1
        print()
