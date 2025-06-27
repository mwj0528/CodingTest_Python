from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x, y = queue.popleft()          
            
        for i in range(4):
            nx, ny = x +dx[i], y+dy[i]
                
            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((nx, ny))
    if maps[n-1][m-1] == 1:
            return -1
    else: 
        return maps[n-1][m-1]
