def solution(n, times):
    left = 0;
    right = min(times) * n;
    answer = right;
    while left <= right:
        mid = (left+right)//2;
        people = 0;
        for time in times:
            people += mid // time;
            if people >= n:
                break;
        if people>=n:
            right = mid-1;
            answer = mid;
        else:
            left = mid+1;
    return answer