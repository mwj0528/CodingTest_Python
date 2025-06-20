from collections import deque
N = int(input())
graph = [list(map(int,input())) for _ in range(N)]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = -1
    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = -1
                    cnt += 1
    return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])