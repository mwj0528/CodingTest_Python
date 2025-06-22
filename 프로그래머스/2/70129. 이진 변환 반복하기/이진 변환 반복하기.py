def solution(s):
    zero_cnt = 0
    cnt = 0
    while True:
        if s == '1':
            break
        num = ""
        for i in range(len(s)):
            if s[i] == '0':
                zero_cnt += 1
                continue
            else:
                num += s[i]
        
        ans = len(num)
        s = bin(ans)[2:]
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer