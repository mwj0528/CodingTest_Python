# [x,y] 라고 하면 max(x)구하기 -> x,y 중 큰 값이 max(x) 보다 작으면 배열 맞추기 
def solution(sizes):
    x = []
    y = []
    for i in sizes:
        i.sort()
        
    for i,j in sizes:
        x.append(i)
        y.append(j)
    
    answer = max(x) * max(y)
    return answer