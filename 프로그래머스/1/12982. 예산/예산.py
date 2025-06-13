# 적은 예산을 가진 팀들을 먼저 지원해주면 된다
def solution(d, budget):
    d.sort()
    
    while budget < sum(d):
        d.pop()
        
    return len(d)