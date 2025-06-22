def solution(s):
    
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        return 1
    else:
        return 0