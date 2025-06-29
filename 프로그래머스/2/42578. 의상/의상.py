def solution(clothes):
    dic = {}
    for cloth in clothes:
        v, k = cloth[0], cloth[1]
        if k in dic:
            dic[k] += [v]
        else:
            dic[k] = [v]
    
    answer = 1
    for _, value in dic.items():
        answer *= (len(value) + 1)
    
    return answer - 1