s = input()
print(s)
for i in range(1,len(s)):
    print(s[-i:]+s[:-i])
print(s)