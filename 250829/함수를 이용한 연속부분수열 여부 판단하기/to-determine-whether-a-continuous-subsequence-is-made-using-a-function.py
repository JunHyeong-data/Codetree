n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(list_a, list_b):

    n1 = len(list_a)
    n2 = len(list_b)
    for i in range(n1 - n2 + 1):
        if  list_a[i : i + n2] == list_b:
            return True
    return False

if func(a, b):
    print('Yes')
else:
    print('No')

    
