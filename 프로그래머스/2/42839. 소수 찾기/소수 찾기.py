from itertools import permutations
def is_prime(num):
    if num  < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = []
    num_lst = list(numbers)
    temp = []
    for i in range(1, len(num_lst)+1):
        temp += list(permutations(num_lst,i))
    num = [int(''.join(t)) for t in temp]
    
    for i in num:
        if is_prime(i):
            answer.append(i)
    return len(set(answer))