def solution(s):
    lst = list(map(ord, s))
    lst.sort(reverse = True)
    
    ans_lst = list(map(chr, lst))
    
    answer = ''.join(ans_lst)
    return answer