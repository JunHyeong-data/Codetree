n = int(input())

# Please write your code here.
def five(n):
    s = str(n)
    st = 0
    for elem in s:
        st += int(elem)
    if st % 5 == 0:
        return True
def sec(n):
    if n % 2 == 0:
        return True

if sec(n) and five(n):
    print('Yes')
else:
    print('No')
