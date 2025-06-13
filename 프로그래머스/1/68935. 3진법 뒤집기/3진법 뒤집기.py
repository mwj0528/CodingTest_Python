def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    
    answer = int(str(rev_base),3)
    return answer