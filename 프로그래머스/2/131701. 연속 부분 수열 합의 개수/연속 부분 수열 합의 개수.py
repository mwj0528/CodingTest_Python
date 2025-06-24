def solution(elements): 
    len_elements = len(elements) # 5
    elements *= 2 # 7 9 1 1 4 7 9 1 1 4
    result = set()
    
    for i in range(len_elements):
        for j in range(len_elements):
            result.add(sum(elements[j:j+i+1]))
    
    return len(result)