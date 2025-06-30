from collections import deque
def solution(n, computers):
    def bfs(start):
        queue = deque()
        queue.append(start)
        while queue:
            com = queue.popleft()
            visited[com] = True
            
            for connect in range(n):
                if connect != com and computers[com][connect] == 1:
                    if visited[connect] == False:
                        visited[connect] = True
                        queue.append(connect)
    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer += 1
    return answer
            

