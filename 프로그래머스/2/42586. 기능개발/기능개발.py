from collections import deque
def solution(progresses, speeds):
    day = []
    answer = []
    for idx, progress in enumerate(progresses):
        rest = 100 - progress
        if rest % speeds[idx] == 0:
            day.append(rest // speeds[idx])
        else:
            day.append(rest // speeds[idx] + 1)
    print(day)       
    
    current = day[0]
    cnt = 1

    for i in range(1, len(day)):
        if day[i] <= current:
            cnt += 1
        else:
            answer.append(cnt)
            current = day[i]
            cnt = 1

    answer.append(cnt)  # 마지막 남은 기능들 배포
    return answer