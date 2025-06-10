def solution(phone_number):
    pn = list(phone_number)
    for i in range(len(pn) - 4):
        pn[i] = '*'
    answer = ''.join(pn)
    return answer