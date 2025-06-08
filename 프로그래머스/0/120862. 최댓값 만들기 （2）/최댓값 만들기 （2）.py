def solution(numbers):
    numbers.sort()
    ans1 = numbers[0] * numbers[1]
    ans2 = numbers[-1] * numbers[-2]
    
    answer = ans1 if ans1 > ans2 else ans2

    return answer