from collections import deque
def solution(progresses, speeds):
    rest = [100-i for i in progresses]
    queue = deque()
    for i in range(len(rest)):
        if rest[i] % speeds[i] == 0:
            queue.append(rest[i] // speeds[i])
        else:
            queue.append(rest[i] // speeds[i] + 1)
    
    answer = []
    
    while queue:
        current = queue.popleft()
        count = 1
        
        # 앞 기능이 끝나는 날(current)보다 작거나 같은 기능은 함께 배포
        while queue and queue[0] <= current:
            queue.popleft()
            count += 1
        
        answer.append(count)
    
    return answer