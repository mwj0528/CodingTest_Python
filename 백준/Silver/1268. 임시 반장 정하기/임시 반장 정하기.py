# 1268
n = int(input())
student = []

for _ in range(n):
    stu = list(map(int, input().split()))
    student.append(stu)

answer = [[0 for _ in range(n)] for _ in range(n)]

for k in range(5): # k학년
    for i in range(n): # i번째 학생
        for j in range(i+1, n): 
            if student[i][k] == student[j][k]:
                answer[j][i] = 1
                answer[i][j] = 1
count = []
for a in answer:
    count.append(a.count(1))

print(count.index(max(count)) + 1)