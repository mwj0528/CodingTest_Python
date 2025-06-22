# 7562
from collections import deque

def bfs(x,y, x_t, y_t,I):
    queue = deque()
    queue.append((x,y))
    visited = [[-1] * I for _ in range(I)]
    visited[y][x] = 0
    while queue:
        x,y = queue.popleft()
        if x == x_t and y == y_t:
            return visited[y][x]
            
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, 2, 1, -1, -2]
    
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
    
            if 0 <= nx < I and 0 <= ny < I:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx,ny))
    return -1
    
T = int(input())
for _ in range(T):
    I =int(input())
    x, y = map(int, input().split())
    x_t, y_t = map(int, input().split())
    print(bfs(x,y, x_t, y_t, I))