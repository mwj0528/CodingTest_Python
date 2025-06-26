# h번 이사 인용된 논문이 h편 이상 -> h의 최댓값이 h-index
# [6,5,3,1,0]
# [0 1 2 3 4] 
def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i + 1 > c:
            return i
    return len(citations)