def solution(s):
    answer = True
    s = s.lower()
    print(s)
    p, y = 0, 0
    for i in s:
        if i == 'p':
            p += 1
        if i == 'y':
            y += 1
    if p == y:
        return True
    else:
        return False