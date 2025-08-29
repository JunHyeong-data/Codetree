def is_date_valid(M, D):
    if not (1 <= M <= 12):
        return False
        
    if D < 1:
        return False

    if M in [1, 3, 5, 7, 8, 10, 12]:
        if D > 31:
            return False
    elif M in [4, 6, 9, 11]:
        if D > 30:
            return False
    elif M == 2:
        if D > 28:
            return False

    return True

M, D = map(int, input().split())

if is_date_valid(M, D):
    print("Yes")
else:
    print("No")