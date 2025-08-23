# N과 a를 입력받기
N, a = map(int, input().split())

# while문을 위한 변수 초기화
i = 1

# 1부터 N까지 반복
while i <= N:
    # i가 a의 배수인지 확인
    if i % a == 0:
        print(1)
    else:
        print(0)
    
    # 다음 숫자로 이동
    i += 1