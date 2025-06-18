while True:
    num = int(input())
    if num < 25:
        print("Higher")
    elif num > 25:
        print("Lower")
    else: # num == 25
        print("Good")
        break