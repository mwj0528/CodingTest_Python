# 1697
from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
def bfs():
    queue = deque()
    queue.append(N)
    visited[N] = 0
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for i in [1, -1, x]:
            nx = x + i
            if 0 <= nx <= 100000 and visited[nx] == -1:
                queue.append(nx)
                visited[nx] = visited[x] + 1
                
print(bfs())