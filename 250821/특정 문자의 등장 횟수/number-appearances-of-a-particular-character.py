s = input()
cnt = 0
cnt2 = 0
for i in range(1,len(s)):
    if s[i] == 'e' and s[i-1] == 'e':
        cnt += 1
for j in range(1,len(s)):
    if s[j] == 'b' and s[j-1] == 'e':
        cnt2 += 1



print(cnt, cnt2)