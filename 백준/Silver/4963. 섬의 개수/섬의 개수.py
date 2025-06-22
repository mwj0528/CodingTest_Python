# 4963
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[y][x] = 0
    while queue:
        x, y = queue.popleft()
        dx = [1, -1, 0, 0, 1, -1, 1, -1]
        dy = [0, 0, 1, -1, 1, -1, -1, 1]

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)