from collections import deque
def solution(n, computers):
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = True
        
        while queue:
            com = queue.popleft()
            visited[com] = True
            for connect in range(n):
                if connect != com and computers[com][connect] == 1:
                    if visited[connect] == False:
                        queue.append(connect)
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer += 1
    return answer
