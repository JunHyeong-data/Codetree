# 변수 선언, 입력
cnt3, cnt5 = 0, 0

for _ in range(10):
	a = int(input())
	
	if a % 3 == 0:
		cnt3 += 1
	if a % 5 == 0:
		cnt5 += 1

# 출력
print(cnt3, cnt5)
