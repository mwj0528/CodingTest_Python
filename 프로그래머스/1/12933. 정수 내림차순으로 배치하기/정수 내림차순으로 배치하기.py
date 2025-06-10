def solution(n):
    str_lst = list(map(int, str(n)))
    str_lst = sorted(str_lst)
    answer = 0
    
    for i in range(len(str_lst)):
        answer += str_lst[i]*(10**i) 
    return answer