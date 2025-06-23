# xy = yellow
# 2x + 2y + 4 = brown
# x >= y
def solution(brown, yellow):
    
    for x in range(3, yellow + brown + 1):
        for y in range(3, x+1):
            if (x-2) * (y-2) == yellow and (2 * (x+y) - 4) == brown:
                return [x,y]
