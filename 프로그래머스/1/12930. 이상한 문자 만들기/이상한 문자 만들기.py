def solution(s):
    answer = ''
    word = s.split(" ")
    print(word)
    for i in word:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()

            else:
                answer += i[j].lower()
        answer += " "
    return answer[:-1]