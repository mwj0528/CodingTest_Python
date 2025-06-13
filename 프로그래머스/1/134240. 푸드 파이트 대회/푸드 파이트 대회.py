def solution(food):
    answer = ''
    for i in range(len(food)):
        food[i] //= 2
        answer += str(i) * food[i]
    reverse = answer[::-1]

    answer += '0'
    answer += reverse
    
    return answer