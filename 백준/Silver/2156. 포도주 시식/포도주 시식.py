# 2156
n = int(input())
q = []
for _ in range(n):
    q.append(int(input()))

d = [0] * n

if n == 1:
    print(q[0])
else:
    d[0] = q[0]
    d[1] = q[0] + q[1]
    
    if n > 2:
        d[2] = max(q[2]+q[1], q[2] + q[0], d[1])
    
    for i in range(3, n):
        d[i] = max(d[i-1], q[i] + d[i-2], q[i] + q[i-1]+d[i-3])
    print(d[-1])