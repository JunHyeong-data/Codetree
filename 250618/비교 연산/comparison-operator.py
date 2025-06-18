# 두 정수 A, B를 공백으로 구분하여 입력받습니다.
A, B = map(int, input().split())

# A가 B보다 같거나 클까? (A >= B)
if A >= B:
    print(1)
else:
    print(0)

# A가 B보다 클까? (A > B)
if A > B:
    print(1)
else:
    print(0)

# B가 A보다 같거나 클까? (B >= A)
if B >= A:
    print(1)
else:
    print(0)

# B가 A보다 클까? (B > A)
if B > A:
    print(1)
else:
    print(0)

# A와 B가 같은가? (A == B)
if A == B:
    print(1)
else:
    print(0)

# A와 B가 다른가? (A != B)
if A != B:
    print(1)
else:
    print(0)