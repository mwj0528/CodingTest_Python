from itertools import combinations
def solution(numbers):
    answer = []
    sum_lst = []
    num_lst = list(combinations(numbers, 2))
    for num in num_lst:
        sum_lst.append(sum(num))
    
    return sorted(list(set(sum_lst)))