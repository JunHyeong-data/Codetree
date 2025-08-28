a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def sachik(a, o, c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '/':
        return a // c
    elif o == '*':
        return a * c
    else:
        return False
if sachik(a,o,c) == False:
    print('False')
else: 
    print(f'{a} {o} {c} = ',end='')
    print(sachik(a,o,c))