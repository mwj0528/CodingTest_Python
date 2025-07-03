# 1764
N, M = map(int, input().split())

not_hear = set()
not_see = set()
answer = set()
for _ in range(N):
    not_hear.add(input())
for _ in range(M):
    not_see.add(input())

for i in not_hear:
    if i in not_see:
        answer.add(i)
print(len(answer))
for i in sorted(answer):
    print(i)