def solution(arr):
    answer = []
    idx = arr.index(min(arr))
    for i in range(len(arr)):
        if i != idx:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    return answer