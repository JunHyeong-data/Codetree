n = int(input())

# Please write your code here.
def s(n):
    num = 0
    for i in range(1, n+1):
        num += i
    return num // 10

print(s(n))