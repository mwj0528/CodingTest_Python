def solution(my_string, n):
    str_lst = list(my_string)
    answer = []
    for i in str_lst:
        answer.append(i*n)
    
    return "".join(answer)