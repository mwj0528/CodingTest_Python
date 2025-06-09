def solution(bin1, bin2):
    res1 = int(bin1,2)
    res2 = int(bin2,2)
    res = bin(res1 + res2)
     
    answer = ''.join(res)
    return answer[2:]