def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[i] * B[-(i+1)]
    return answer