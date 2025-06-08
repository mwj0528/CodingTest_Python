def solution(array, n):
    
    answer = []
    dict = {}
    
    for i in array:
        dict[i] = abs(n-i)
    
    dict_min = min(dict.values())
    for a, b in dict.items():
        if b == dict_min:
            answer.append(a)
    return min(answer)
        