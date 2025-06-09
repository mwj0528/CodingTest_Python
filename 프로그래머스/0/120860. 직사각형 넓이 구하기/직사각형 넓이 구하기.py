def solution(dots):
    answer = 0
    x, y = 0, 0
    for i in range(3):
        for j in range(i+1,4):
            if dots[i][0] == dots[j][0]:
                y = abs(dots[i][1] - dots[j][1])
            if dots[i][1] == dots[j][1]:
                x = abs(dots[i][0] - dots[j][0])
    
    answer = x * y        
    return answer