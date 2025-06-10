def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        cnt = 0
        for i in range(1, int(num ** 0.5)):
            if num % i == 0:
                cnt += 2
        if (num ** 0.5) == int(num ** 0.5):
            cnt += 1
        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer