from collections import deque

def solution(tickets):
    tickets.sort()  # 사전순 우선순위 보장
    n = len(tickets)
    queue = deque()
    queue.append(("ICN", ["ICN"], tickets))

    while queue:
        curr, path, remain = queue.popleft()
        
        if not remain:  # 모든 티켓을 다 썼으면 정답
            return path

        for i in range(len(remain)):
            dep, arr = remain[i]
            if dep == curr:
                next_remain = remain[:i] + remain[i+1:]  # i번째 티켓 사용
                queue.append((arr, path + [arr], next_remain))
    
    return []
