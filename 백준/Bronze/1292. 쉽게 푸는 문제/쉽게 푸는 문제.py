# 1292
a, b = map(int, input().split())
answer = 0
num_lst = []
i = 1
while len(num_lst) < b:
    for _ in range(i):
        num_lst.append(i)
    i += 1
print(sum(num_lst[a-1:b]))