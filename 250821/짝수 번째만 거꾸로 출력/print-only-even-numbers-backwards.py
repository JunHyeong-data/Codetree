s = input()

if len(s) % 2 == 0:
    for i in s[::-2]:
        print(i, end='')
else:
    for i in s[-2::-2]:
        print(i, end='')