def solution(x):
    x_lst = [i for i in str(x)]
    x_lst = list(map(int, x_lst))
    x_sum = sum(x_lst)
    if x % x_sum == 0:
        answer = True
    else:
        answer = False
    return answer