def solution(rsp):
    lst = []
    for i in rsp:
        if i == '0':
            lst.append('5')
        elif i == '2':
            lst.append('0')
        else:
            lst.append('2')
    answer = ''.join(lst)
    return answer