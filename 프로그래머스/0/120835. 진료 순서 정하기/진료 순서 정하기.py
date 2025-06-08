def solution(emergency):
    sort_emergency = sorted(emergency, reverse = True)
    answer = [0] * len(emergency)
    for i in range(len(sort_emergency)):
        order = i + 1
        for j in range(len(emergency)):
            if emergency[j] == sort_emergency[i]:
                answer[j] = order
    
    return answer