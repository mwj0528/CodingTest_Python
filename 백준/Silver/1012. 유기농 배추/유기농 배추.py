import sys
sys.setrecursionlimit(10000)  # 깊은 재귀를 위한 설정

def dfs(x, y):
    graph[x][y] = 2  # 현재 위치 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)  # 인접한 배추도 DFS로 방문
    return 1

# 테스트 케이스 수만큼 반복
for _ in range(int(input())):
    m, n, k = map(int, input().split())  # 가로(m), 세로(n), 배추 개수(k)
    graph = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    # 배추 심기
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += dfs(i, j)  # 새로운 덩어리 발견 시 DFS 실행

    print(cnt)
