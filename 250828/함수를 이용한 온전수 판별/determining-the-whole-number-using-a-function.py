a, b = map(int, input().split())

# Please write your code here.
def onjeon(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif (n % 3 == 0) and (n % 9 != 0):
        return False
    return True

def func(a, b):
    cnt = 0
    for i in range(a, b+1):
        if onjeon(i):
            cnt += 1
    return cnt
print(func(a,b))
