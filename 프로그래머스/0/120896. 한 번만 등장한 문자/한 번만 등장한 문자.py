import bisect
def solution(s):
    str_lst = list(s)
    str_lst.sort()
    answer = []
    for i in str_lst:
        if bisect.bisect(str_lst,i) - bisect.bisect_left(str_lst,i) == 1:
            answer.append(i)
    
    return "".join(answer)