a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True

def even_sum(n):
    ev = str(n)
    tot = 0
    for i in ev:
        tot += int(i)
    if tot % 2 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if is_prime(i):
        if even_sum(i):
            cnt += 1
print(cnt)

            
