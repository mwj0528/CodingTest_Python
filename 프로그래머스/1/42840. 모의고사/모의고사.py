def solution(answers):
    answer = []
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    if len(answers) > 10:
        ans_1 *= (len(answers) // 5 + 1)
        ans_2 *= (len(answers) // 8 + 1)
        ans_3 *= (len(answers) // 10 + 1)
        
    elif len(answers) > 8:
        ans_1 *= (len(answers) // 5 + 1)
        ans_2 *= (len(answers) // 8 + 1)
    elif len(answers) > 5:
        ans_1 *= (len(answers) // 5 + 1)
    ans_1 = ans_1[:len(answers)]
    ans_2 = ans_2[:len(answers)]
    ans_3 = ans_3[:len(answers)]
    
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    for i in range(len(answers)):
        if ans_1[i] == answers[i]:
            cnt_1 += 1
        if ans_2[i] == answers[i]:
            cnt_2 += 1
        if ans_3[i] == answers[i]:
            cnt_3 += 1
    
    cnt = [cnt_1, cnt_2, cnt_3]
    max_cnt = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == max_cnt:
            answer.append(i+1)
    return answer