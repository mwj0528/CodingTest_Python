def solution(n):
    
    cnt = bin(n)[2:].count('1')
    while True:
        n += 1
        nxt_bin = bin(n)[2:]
        nxt_cnt = bin(n)[2:].count('1')
        if cnt == nxt_cnt:
            break
    answer = n
    return answer