from collections import Counter
def solution(array):
    answer = 0
    for i in array:
        counter = Counter(str(i))
        answer += counter['7']
    return answer