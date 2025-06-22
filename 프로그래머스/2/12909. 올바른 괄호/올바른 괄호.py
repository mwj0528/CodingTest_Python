def solution(s):
    stack = []
    str_lst = list(s)
    for i in range(len(str_lst)):
        if str_lst[i] == '(':
            stack.append(str_lst[i])
        elif str_lst[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(str_lst[i])
    if len(stack) == 0:
        return True
    else:
        return False