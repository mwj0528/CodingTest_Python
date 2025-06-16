import math
# 소수 판별
def is_prime(x):
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    return True

def solution(n):
    cnt = 0
    for i in range(2,n+1):
        if is_prime(i):
            cnt += 1
    return cnt