def solution(n, arr1, arr2):
    arr1_bi = []
    arr2_bi = []
    answer = []
    for i in range(n):
        if len(bin(arr1[i])[2:]) != n:
            a = '0' *(n - len(bin(arr1[i])[2:])) + bin(arr1[i])[2:]
            arr1_bi.append(a)
        else:
            arr1_bi.append(bin(arr1[i])[2:])
        if len(bin(arr2[i])[2:]) != n:
            b = '0' *(n - len(bin(arr2[i])[2:])) + bin(arr2[i])[2:]
            arr2_bi.append(b)
        else:
            arr2_bi.append(bin(arr2[i])[2:])
        
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1_bi[i][j] == '1' or arr2_bi[i][j] == '1':
                temp += '#'
            elif arr1_bi[i][j] == '0' and arr2_bi[i][j] == '0':
                temp += ' '
        answer.append(temp)

    return answer