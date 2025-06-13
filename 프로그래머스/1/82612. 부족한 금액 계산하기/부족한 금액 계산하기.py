def solution(price, money, count):
    answer = -1
    fee = 0
    for i in range(1, count+1):
        fee += (price * i)
    answer = fee - money
    if answer <= 0:
        return 0

    return answer