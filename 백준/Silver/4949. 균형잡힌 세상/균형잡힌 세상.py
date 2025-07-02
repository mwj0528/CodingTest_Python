# 4949
def check(sen):
    for i in range(len(sen)):
        if sen[i] == '(':
            stack.append('(')
        if sen[i] == '[':
            stack.append('[')
        if sen[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        if sen[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    if len(stack) != 0:
        print('no')
    else:
        print('yes')

while True:
    sen = input()
    if sen == '.':
        break
    stack = []
    check(sen)