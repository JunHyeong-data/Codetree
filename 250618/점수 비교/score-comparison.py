# A의 수학과 영어 점수를 입력받습니다.
A_math, A_english = map(int, input().split())

# B의 수학과 영어 점수를 입력받습니다.
B_math, B_english = map(int, input().split())

# A가 B보다 수학 점수도 크고 영어 점수도 큰지 확인합니다.
if A_math > B_math and A_english > B_english:
    print(1)
else:
    print(0)