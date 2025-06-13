# a병을 주면 b병을 주는 마트에 n병을 주면 몇병을 받을지
def solution(a, b, n):
    answer = 0
    temp = 0
    while n >= a:
        new_bottle = (n // a) * b
        answer += new_bottle
        n = (n % a) + new_bottle   # 남은 병 + 새로 받은 병 => 다음 교환 가능 병
    
    return answer