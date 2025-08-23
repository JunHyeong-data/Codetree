s = list(input())

leng = len(s)
while True:
    if leng == 1:
        break
    index = int(input())
    if index > leng:
        s.pop(-1)
    else:
        s.pop(index)
    print(''.join(s))
    leng -= 1