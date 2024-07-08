def check(stones, mid,k):
    cnt = 0;
    for stone in stones:
        if (stone - mid) <= 0:
            cnt += 1;
        else:
            cnt = 0;
        if cnt>=k:
            return False;
    return True;

def solution(stones, k):
    start,end = 1,max(stones);
    answer = 0;
    while start<=end:
        mid = (start + end) // 2;
        if check(stones, mid,k):
            start = mid+1;
        else:
            answer = mid;
            end = mid-1;    
    return answer;