a, b = map(int, input().split())

# Please write your code here.
def fun(n):
    return n // 10 == 3 or n //10 ==6 or n//10 ==9

def func(n):
    return n % 10 == 3 or n % 10 == 6 or n%10 ==9
def game(a, b):
    cnt = 0
    for i in range(a, b+1):
        if fun(i) or func(i) or i % 3 == 0:
            cnt += 1
    return cnt

print(game(a,b))