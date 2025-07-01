# 1296
name = input()
n = int(input())
teams = []
for _ in range(n):
    teams.append(input())
teams.sort()
result = teams[0]
result_p = 0
for team in teams:
    L = name.count('L')
    O = name.count('O')
    V = name.count('V')
    E = name.count('E')
    L += team.count('L')
    O += team.count('O')
    V += team.count('V')
    E += team.count('E')
    p = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if p > result_p:
        result_p = p
        result = team
    elif p == result_p:
        result = min(result, team)
print(result)