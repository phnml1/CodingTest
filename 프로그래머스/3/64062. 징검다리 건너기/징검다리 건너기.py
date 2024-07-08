def continuity(stones, mid,k):
    cnt = 0;
    for stone in stones:
        if (stone - mid) <= 0:
            cnt += 1;
        else:
            cnt = 0;
        if cnt>=k:
            break;
    return cnt;

def solution(stones, k):
    start,end = 1,max(stones);
    answer = 0;
    while start<=end:
        mid = (start + end) // 2;
        if continuity(stones, mid,k) < k:
            start = mid+1;
        else:
            answer = mid;
            end = mid-1;    
    return answer;