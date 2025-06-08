def solution(my_string):
    str_lst = list(my_string)
    answer = []
    
    for i in str_lst:
        if i not in answer:
            answer.append(i)
    
    return "".join(answer)