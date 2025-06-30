from collections import deque
def solution(maps):
    n = len(maps[0])
    m = len(maps)
    def bfs():
        queue = deque()
        queue.append((0,0))
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        queue.append((nx, ny))
        
        return maps[m-1][n-1]
    result = bfs()
    if result == 1:
        return -1
    return result