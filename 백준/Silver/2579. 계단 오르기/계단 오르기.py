N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))

score = [0] * (N+1)
score[1] = stair[1]

if N >= 2:
    score[2] = stair[1] + stair[2]
for i in range(3,N+1):
    score[i] = max(score[i-2] + stair[i], score[i-3] + stair[i-1] + stair[i])

print(score[-1])