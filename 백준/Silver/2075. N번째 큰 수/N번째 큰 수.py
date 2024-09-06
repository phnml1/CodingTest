import sys;
import heapq
input = sys.stdin.readline;

n = int(input());
arr = [];
for _ in range(n):
    cur = list(map(int,input().split()));
    for a in cur:
        if len(arr) < n:
            heapq.heappush(arr,a);
        else:
            if a>arr[0]:
                heapq.heappop(arr);
                heapq.heappush(arr,a);
print(arr[0]);