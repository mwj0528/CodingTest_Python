def solution(num, k):
    num_lst = list(str(num))
    answer = -1
    for i in range(len(num_lst)):
        
        if num_lst[i] == str(k):
            answer = i+1
            break
        else:
            answer = -1
    return answer