from itertools import permutations
def solution(numbers):
    answer = ''
    str_num = [str(i) for i in numbers]
    str_num = sorted(str_num, key=lambda x: x*3, reverse = True)
    if str_num[0] == '0':
        return '0'
    for i in str_num:
        answer += i
    return answer