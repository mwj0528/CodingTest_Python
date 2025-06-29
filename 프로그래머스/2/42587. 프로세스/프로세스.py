# popleft
# 우선 순위가 1순위가 아니다? -> 다시 append(맨뒤로)
# 1순위다? -> continue
# location의 idx에 있는 프로세스가 몇번째로 실행되는지 return
from collections import deque
def solution(priorities, location):
    queue = deque((i, p) for i,p in enumerate(priorities))
    print(queue)
    
    answer = 0
    while queue:
        process = queue.popleft()
        if any(process[1]<other[1] for other in queue):
            queue.append(process)
        else:
            answer += 1
            if process[0] == location:
                return answer
