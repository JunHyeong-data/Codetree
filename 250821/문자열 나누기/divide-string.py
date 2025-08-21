n = int(input())
s = input().split()
combined = ""
for i in s:
    combined += i

cnt = 0
for i in combined:
    print(i, end='')
    cnt += 1
    if cnt == 5:
        print()
        cnt = 0
    
