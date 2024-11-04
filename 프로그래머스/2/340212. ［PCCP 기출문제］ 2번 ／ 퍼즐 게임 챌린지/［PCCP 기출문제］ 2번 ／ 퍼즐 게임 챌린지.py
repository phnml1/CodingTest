def solution(diffs, times, limit):
    max_diff = max(diffs);
    r = max_diff;
    l = 1;
    answer = max_diff;
    while l<r:
        level = (l+r)//2;
        time = times[0];
        for i in range(1,len(times)):
            false_count = diffs[i] - level;
            k = 0;
            if false_count > 0:
                k = (times[i-1] + times[i]) * false_count;
            time += (k + times[i]);
        if time<=limit:
            answer = level;
            r = level;
        else:
            l = level + 1;
    return answer;