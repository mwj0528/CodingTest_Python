def solution(N, stages):
    answer = []
    sum_list = [0] * (N+2)  # 인덱스: 스테이지 번호, 값: 해당 스테이지에 있는 사람 수
    dic_list = {}  # 스테이지별 실패율 저장

    stages.sort()  # O(n log n), 정렬로 탐색이 쉬움
    now = len(stages)  # 현재 스테이지에 도달한 사람 수

    # 각 스테이지에 있는 사람 수 기록
    for i in stages:
        sum_list[i] += 1
    
    # 각 스테이지 실패율 계산
    for i in range(1, N+1):
        if now == 0:
            dic_list[i] = 0
        else:
            dic_list[i] = sum_list[i] / now
            now -= sum_list[i]  # 다음 스테이지로 갈 사람 수 줄임
    
    # 실패율 기준으로 내림차순 정렬한 스테이지 리스트 반환
    return sorted(dic_list, key=lambda x: dic_list[x], reverse=True)
