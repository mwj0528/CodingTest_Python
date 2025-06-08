def solution(my_string, num1, num2):
    lst = []
    for i in my_string:
        lst.append(i)
    tmp = lst[num1]
    lst[num1] = lst[num2]
    lst[num2] = tmp
    answer = "".join(lst)
    return answer