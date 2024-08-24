import sys;
import heapq;

input = sys.stdin.readline;
n = int(input());
arr = [];
for _ in range(n):
  x = int(input());
  if x>0:
    heapq.heappush(arr,x);
  else:
    if len(arr) == 0:
      print(0);
      continue;
    print(heapq.heappop(arr));