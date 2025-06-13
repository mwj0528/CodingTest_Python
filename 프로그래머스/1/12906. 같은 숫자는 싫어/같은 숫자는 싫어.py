def solution(arr):
    stack = [arr[0]]
    for i in range(len(arr)):
        if arr[i] != stack[-1]:
            stack.append(arr[i])
        else:
            continue
    
    return stack