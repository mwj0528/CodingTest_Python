def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        tmp = A[i] * B[i]
        answer += tmp    
    return answer