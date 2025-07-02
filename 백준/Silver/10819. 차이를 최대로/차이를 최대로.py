# 10819
from itertools import permutations

N = int(input())
num = list(map(int, input().split()))

max_val = 0

for perm in permutations(num):
    total = 0
    for i in range(N-1):
        total += abs(perm[i] - perm[i+1])
    max_val = max(max_val, total)
print(max_val)