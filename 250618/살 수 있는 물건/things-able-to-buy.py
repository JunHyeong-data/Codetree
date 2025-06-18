# 가지고 있는 돈 N을 입력받습니다.
N = int(input())

# 물건들의 가격을 정의합니다.
book_price = 3000
mask_price = 1000

# 책을 살 수 있는지 확인합니다.
can_buy_book = (N >= book_price)
# 마스크를 살 수 있는지 확인합니다.
can_buy_mask = (N >= mask_price)

# 가장 비싼 물건을 출력해야 하므로, 우선순위를 둡니다.
if can_buy_book:
    print("book")
elif can_buy_mask: # 책은 살 수 없고, 마스크는 살 수 있을 때
    print("mask")
else: # 아무것도 살 수 없을 때
    print("no")