# popleft했는데 더 큰 수가 proprities에 있으면 다시 append
# 없으면 실행
from collections import deque
def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    cnt = 0
    while queue:
        cur = queue.popleft()
        if any(cur[0] < other[0] for other in queue):
            queue.append(cur)
        else:
            cnt += 1
            if cur[1] == location:  # 내가 찾던 프로세스라면
                return cnt