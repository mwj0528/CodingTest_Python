# 11724
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
cnt = 0
for i in range(1,N+1):
    if visited[i] == False:
        bfs(i)
        cnt += 1
print(cnt)
            