# 2529
from itertools import permutations

k = int(input())
A = list(input().split())
nums = [i for i in range(10)]

def is_valid(a, b, op):
    if op == '<':
        if a > b: return False
    if op == '>':
        if a < b: return False
    return True

new_nums = []
for perm in permutations(nums, k+1):
    check = True
    for i in range(k):
        if not is_valid(perm[i], perm[i+1], A[i]):
            check = False
            break
    if check == True:
        n = ''.join(map(str, perm))
        new_nums.append(n)
new_nums.sort()
print(new_nums[-1])
print(new_nums[0])