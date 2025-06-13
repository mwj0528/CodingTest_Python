import math
def solution(n, m):
    gcd = math.gcd(n,m)
    bcm = n * m / gcd
    answer = [gcd, bcm]
    return answer