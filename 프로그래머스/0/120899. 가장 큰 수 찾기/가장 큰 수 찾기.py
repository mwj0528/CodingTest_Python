def solution(array):
    
    arr_max = max(array)
    
    for i in range(len(array)):
        if array[i] == arr_max:
            idx = i
    answer = [arr_max, idx]
    return answer