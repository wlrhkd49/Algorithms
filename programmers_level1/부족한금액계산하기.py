def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer+=i
    if price*answer < money:
        return 0
    else:
        return price*answer - money
