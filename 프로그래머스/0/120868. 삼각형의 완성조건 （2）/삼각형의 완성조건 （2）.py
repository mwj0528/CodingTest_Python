# a < b < c  -> c < a+b

def solution(sides):
    answer = 0
    a, b = sides[0], sides[1]
    max_num = max(a,b)
    min_num = min(a,b)
    for i in range(1, max_num+1):
        if min_num + i > max_num:
            answer += 1
    for i in range(max_num+1, sum(sides)):
        if sum(sides) > i:
            answer += 1
        
    return answer