from itertools import combinations
def solution(number):
    answer = 0
    example = list(combinations(number, 3))
    for i in example:
        if sum(i) == 0:
            answer += 1
        
    return answer