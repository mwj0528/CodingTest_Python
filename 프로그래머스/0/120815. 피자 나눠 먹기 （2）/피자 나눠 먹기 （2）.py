# 6과 n의 최소공배수 / 6
# 최소공배수: 6 * n / gcd(6,n)
import math
def solution(n):
    answer = (6 * n / math.gcd(6, n)) / 6
    
    return answer