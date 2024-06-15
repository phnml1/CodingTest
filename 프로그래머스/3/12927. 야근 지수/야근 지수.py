import heapq
import math
def solution(n, works):
    answer = 0;
    if sum(works)<=n:
        return 0;
    works = [-w for w in works];
    heapq.heapify(works)
    for i in range(n):
        node = heapq.heappop(works);
        cur = abs(node)-1
        heapq.heappush(works,-cur);
    for w in works:
        answer += w**2;
    return answer