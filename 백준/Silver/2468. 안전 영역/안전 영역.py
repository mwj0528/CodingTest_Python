from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]

def bfs(x, y, h, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] > h:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

max_safe = 0

for h in range(0, max(map(max, graph)) + 1):
    visited = [[0]*N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h, visited)
                count += 1

    max_safe = max(max_safe, count)

print(max_safe)
