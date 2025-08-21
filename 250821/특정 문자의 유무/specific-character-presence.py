s = input()
ee = False
ab = False
for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        ee = True
    if s[i:i+2] == 'ab':
        ab = True

if ee == True:
    print('Yes', end=' ')
else:
    print('No', end=' ')
if ab == True:
    print('Yes', end=' ')
else:
    print('No', end=' ')