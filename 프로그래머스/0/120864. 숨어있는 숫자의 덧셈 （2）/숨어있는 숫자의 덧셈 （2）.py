def solution(my_string):
    str_num = []
    answer =  []
    str_lst = list(my_string)
    for i in str_lst:
        if i.isdigit() == False:
            str_num.append(" ")
        else:
            str_num.append(i)
    num_lst = "".join(str_num).split()
    for i in num_lst:
        answer.append(int(i))
    
    return sum(answer)