n = int(input())
cnt1 = n
cnt2 = 1

for i in range(2*n):
    if i % 2 == 0:
        print('* '*cnt1,end='')
        cnt1 -= 1
    else:
        print('* '*cnt2,end='')
        cnt2 += 1
    print()