# 11725
from collections import deque
N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [0] * (N+1)

def bfs():
    queue = deque()
    queue.append(1)
    
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if parent[nxt] == 0:
                parent[nxt] = now
                queue.append(nxt)

bfs()
res = parent[2:]
for x in res:
    print(x)