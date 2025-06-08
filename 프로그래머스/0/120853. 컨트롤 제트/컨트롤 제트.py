def solution(s):
    answer = 0
    num = []
    str = s.split()
    for i in str:
        if i != 'Z':
            num.append(int(i))
        else:
            num.pop()
    return  sum(num)
    