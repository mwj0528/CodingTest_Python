from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    
    for i, v in counter.items():
        if k <= 0:
            return answer
        k -= v
        answer+=1
    return answer