def solution(s):
    answer = ''
    if len(s) % 2 != 0:
        answer = s[(len(s) - 1)//2]
    else:
        answer = s[len(s)//2-1:len(s)//2+1]
    
    return answer