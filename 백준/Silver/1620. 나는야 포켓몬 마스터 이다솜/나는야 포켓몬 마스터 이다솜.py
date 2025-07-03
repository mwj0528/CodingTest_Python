# 1620
N, M = map(int, input().split())

number_to_name = {}
name_to_number = {}

for i in range(1, N + 1):
    name = input()
    number_to_name[i] = name
    name_to_number[name] = i
    
for _ in range(M):
    question = input()
    if question.isdigit():
        print(number_to_name[int(question)])
    else:
        print(name_to_number[question])