from collections import Counter
def solution(order):
    answer = 0
    ord_lst = list(str(order))
    
    counter = Counter(ord_lst)
    
    if counter['3'] != 0 or counter['6'] != 0 or counter['9'] != 0:
        answer += counter['3']
        answer += counter['6']
        answer += counter['9']
        
    return answer