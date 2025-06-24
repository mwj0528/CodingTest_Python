from math import gcd

def solution(arr):
    answer = arr.pop(0)
    
    for num in arr:
        answer = (answer * num) // gcd(answer, num)
    return answer