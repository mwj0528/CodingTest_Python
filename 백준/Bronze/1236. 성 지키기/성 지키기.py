# 1236
N, M = map(int, input().split())
map = []
for _ in range(N):
    map.append(input())

row_cnt, col_cnt = 0, 0

for i in range(N):
    if 'X' not in map[i]:
        row_cnt += 1
        
for j in range(M):
    if 'X' not in [map[i][j] for i in range(N)]:
        col_cnt += 1
print(max(row_cnt, col_cnt))