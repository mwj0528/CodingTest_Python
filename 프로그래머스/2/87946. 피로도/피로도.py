from itertools import permutations
def solution(k, dungeons):
    answer = -1
    
    for perm in permutations(dungeons):
        stamina = k
        cnt = 0
        for need, reduce in perm:
            if stamina >= need:
                stamina -= reduce
                cnt += 1
            if cnt > answer:
                answer = cnt
        
        
    return answer