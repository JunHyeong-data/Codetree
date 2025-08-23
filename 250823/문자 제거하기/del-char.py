s = list(input())

leng = len(s)
while leng != 1:
    index = int(input())
    if index > leng:
        s.pop(-1)
    else:
        s.pop(index)
    print(''.join(s))
    leng -= 1