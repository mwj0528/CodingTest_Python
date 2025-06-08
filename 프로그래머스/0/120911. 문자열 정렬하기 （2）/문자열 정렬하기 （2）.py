def solution(my_string):
    low_str = my_string.lower()
    str_lst = list(low_str)
    
    str_lst.sort()
    
    return "".join(str_lst)