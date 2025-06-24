def true_s(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == '{':
            stack.append(s[i])
        elif s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        elif s[i] == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s[i])
        elif s[i] == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[-1] + s
        s = s[:-1]
        if true_s(s) == True:
            answer += 1
    
    
    return answer