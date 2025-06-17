# 2606
from collections import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False for _ in range(N+1)]
def bfs():
    queue = deque()
    count = 0 # 감염된 컴퓨터 수
    queue.append(1) # 1번부터 시작
    visited[1] = True # 1번 감염 완료

    while queue:
        current = queue.popleft()
        for val in graph[current]: # 감염된 컴퓨터와 연결된 컴퓨터들에서
            if visited[val] == False: # 감염되지 않으면
                queue.append(val) # 감염 리스트에 추가
                visited[val] = True # 감염 완료
                count += 1 # 감염 대수 1개 추가
    print(count)
bfs()