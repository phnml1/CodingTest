def solution(A, B):
    answer = 0
    A.sort(reverse = True);
    B.sort(reverse = True);
    i = 0;
    j = 0;
    while i < len(A) and j< len(B):
        if A[i] < B[j]:
            j+=1;
            i+=1;
            answer += 1;
        else:
            i+=1;
    return answer