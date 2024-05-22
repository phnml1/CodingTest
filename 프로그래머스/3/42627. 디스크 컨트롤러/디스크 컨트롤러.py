import heapq
def solution(jobs):
    queue = [];
    answer = 0
    i = 0;
    now = 0;
    start = -1;
    while i<len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(queue, [job[1],job[0]]);
        if queue:
            current = heapq.heappop(queue);
            start = now;
            now += current[0];
            answer += now - current[1];
            i += 1;
        else:
            now += 1;
    return answer // len(jobs)