def solution(array, commands):
    answer = []
    for command in commands:
        # print(command)
        i,j,k = command[0], command[1], command[2]
        slice_array = array[i-1:j]
        slice_array.sort()
        
        answer.append(slice_array[k-1])
    
    return answer