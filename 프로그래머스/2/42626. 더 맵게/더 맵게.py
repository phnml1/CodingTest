import heapq
def solution(scoville, K):
    answer = 0
    queue = []
    for s in scoville:
        heapq.heappush(queue, s);
    
    while queue:
        s1 = heapq.heappop(queue);
        if s1>=K:
            break;
        if len(queue) == 0:
            answer = -1;
            break;
        s2 = heapq.heappop(queue);
        heapq.heappush(queue,s1 + (2 * s2));
        answer += 1;
    return answer