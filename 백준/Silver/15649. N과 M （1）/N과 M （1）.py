# 15649
from itertools import permutations
N, M = map(int, input().split())
num = [i for i in range(1, N+1)]
answer = list(permutations(num, M))
for i in answer:
    print(*i)