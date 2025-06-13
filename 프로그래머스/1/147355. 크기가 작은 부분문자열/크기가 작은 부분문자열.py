def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if i+len(p) <= len(t):
            num = t[i:i+len(p)]
            if int(num) <= int(p):
                answer += 1
        else:
            break
        
    return answer