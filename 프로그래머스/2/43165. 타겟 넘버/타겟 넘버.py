from collections import deque
def solution(numbers, target):
    answer = 0
    cnt = 0
    queue = deque()
    queue.append((0,0)) # (index, current_sum)

    while queue:
        index, current_sum = queue.popleft()
        
        if index == len(numbers):
            if current_sum == target:
                cnt += 1
        else:
            num = numbers[index]
            queue.append((index+1, current_sum + num))
            queue.append((index+1, current_sum - num))
    return cnt