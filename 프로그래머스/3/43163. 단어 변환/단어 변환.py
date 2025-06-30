from collections import deque
def bfs(begin, target, words):
    queue = deque()
    queue.append([begin,0])
    
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        #단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            cnt = 0
            for i in range(len(now)): #단어의 길이만큼 반복하여
                if now[i] != word[i]: #단어에 알파벳 한개씩 체크하기
                    cnt += 1
                    
            if cnt == 1: 
                queue.append([word, step+1])
                
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    return answer