#다시풀어라
import sys;
import heapq;
input = sys.stdin.readline;

dir = [2,1,-1]
n,k = map(int,input().split());
location = [1e9] * 100001;
queue = [];
heapq.heappush(queue,(0,n));
while queue:
  time,cur = heapq.heappop(queue);
  if cur == k:
    location[k] = time;
    break;
  for i in range(3):
    next_cur,next_time = cur,time;
    if i == 0:
      next_cur *= dir[i];
      next_time += 0;
    else:
      next_cur += dir[i];
      next_time += 1;
    if 0<=next_cur<=100000 and location[next_cur] > next_time:
      heapq.heappush(queue,(next_time,next_cur));
      location[next_cur] = next_time;
print(location[k]);
    