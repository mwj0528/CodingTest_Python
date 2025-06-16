def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    
    for i in range(len(photo)):
        lst = []
        lst = photo[i]
        score = 0
        for j in lst:
            if j in dic.keys():
                score += dic[j]
        answer.append(score)
    return answer