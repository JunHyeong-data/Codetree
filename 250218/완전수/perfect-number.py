start, end = map(int, input().split())  # 입력 받기
count = 0  # 완전수 개수를 저장할 변수

for n in range(start, end + 1):  # start부터 end까지 반복
    divisors_sum = 0  # 약수의 합 초기화
    
    for i in range(1, n // 2 + 1):  # n의 절반까지만 검사 (속도 최적화)
        if n % i == 0:  # i가 n의 약수인지 확인
            divisors_sum += i  # 약수라면 합에 추가

    if divisors_sum == n:  # 약수의 합이 자기 자신과 같으면 완전수
        count += 1

print(count)  # 최종 완전수 개수 출력
