def divisor(number): 
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number//i:
                result.append(number//i)
    return len(result) 
def solution(number, limit, power):
    weapon_lst = []
    for i in range(1, number+1):
        weapon_lst.append(divisor(i))
    
    for i in range(len(weapon_lst)):
        if weapon_lst[i] > limit:
            weapon_lst[i] = power
    
    answer = sum(weapon_lst)
    return answer

