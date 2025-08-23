s = list(input())

for i,elem in enumerate(s):
    if elem == 'e':
        s.pop(i)
        break
print(''.join(s))

