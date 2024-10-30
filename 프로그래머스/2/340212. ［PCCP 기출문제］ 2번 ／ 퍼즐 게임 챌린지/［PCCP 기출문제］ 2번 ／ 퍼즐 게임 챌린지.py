def solution(diffs, times, limit):
    max_level = max(diffs)
    l = 1
    r = max_level;
    answer = max_level;
    while l<r:
        level = (l+r)//2;
        time = times[0]
        for i in range(1,len(diffs)):
            w_count = diffs[i] - level;
            if w_count > 0:
                time += w_count*(times[i-1] + times[i]) + times[i];
            else:
                time += times[i];
        if time>limit:
            l = level+1;
        else:
            r = level;
            answer = level;
    return answer;