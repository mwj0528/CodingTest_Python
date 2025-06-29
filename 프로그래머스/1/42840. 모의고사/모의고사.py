# 1,2,3,4,5,2,3,4
# 0,1,2,3,4,5,6,7
def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    p_1 = [1, 2, 3, 4, 5]
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, cor in enumerate(answers):
        if cor == p_1[idx % len(p_1)]:
            cnt[0] += 1
        if cor == p_2[idx % len(p_2)]:
            cnt[1] += 1
        if cor == p_3[idx % len(p_3)]:
            cnt[2] += 1
    for i, v in enumerate(cnt):
        if v == max(cnt):
            answer.append(i+1)
    return answer