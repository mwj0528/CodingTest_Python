# 2812
N, K = map(int, input().split())
num = input()
stack = []
for i in num:
    while stack and K > 0 and stack[-1] < i:
        stack.pop()
        K -= 1
    stack.append(i)

if K > 0:
    stack = stack[:-K]
print(''.join(stack))