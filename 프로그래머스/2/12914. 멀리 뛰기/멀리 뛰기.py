# n: 1을 n개 배치 / 1을 n-2개 2를 1개 배치 / 1을 n-4개 2를 2개 배치 / ...
# 6: 1 1 1 1 1 1 1 1 / 1 1 1 1 1 1 2 / 1 1 1 1 2 2 / 1 1 2 2 2 / 2 2 2 2
# nC0 + (n-1)C1 + (n-2)C2 + (n-3)C3 + ...(n-4)C4 + ... 
# 3C0 + 2C1 + 1C2
from math import comb
def solution(n):
    answer = 0

    for i in range(n+1):
        if n - i >= i:
            a = comb(n-i,i)
            answer += a
    return answer % 1234567

# 4 -> i = 0 , 1, 2, 3
# 4 - 0 > 0
# 3 - 1 > 0
# 2 - 2
# 4C0 +  3C1 + 