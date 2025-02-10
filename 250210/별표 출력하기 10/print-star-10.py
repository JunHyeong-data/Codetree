n= int(input())
cnt1 = 1
cnt2 = n
for i in range(1,n+1):
    if i % 2 != 0 :
        for j in range (cnt1):
            print('*', end=' ')

        cnt1 += 1
    else :
        for j in range (cnt2):
            print('*', end=' ')
        cnt2 -= 1
    print()
cnt1 -= 1
cnt2 += 1
for i in range(1,n+1):
    if i % 2 != 0 :
        for j in range (cnt1):
            print('*', end=' ')
        cnt1 -= 1
    else :
        for j in range (cnt2):
            print('*', end=' ')
        cnt2 += 1
    print()