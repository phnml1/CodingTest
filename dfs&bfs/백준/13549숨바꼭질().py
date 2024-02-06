import sys
import heapq
input = sys.stdin.readline;
n,k  = map(int,input().split());
max_map = 100000;
distance = [1e9 for _ in range(max_map+1)];
queue = [];
heapq.heappush(queue,(0,n));
while queue:
  cost,now = heapq.heappop(queue);
  if now == k:
    distance[now] = cost;
    break;
  if distance[now] < cost:
    continue;
  if 0<=now*2<=max_map and distance[now*2]>cost:
    heapq.heappush(queue,(cost,now*2));
    distance[now*2] = cost
  if now+1<=max_map and distance[now+1]>cost+1:
    heapq.heappush(queue,(cost+1,now+1));
    distance[now+1] = cost+1
  if now-1>=0 and distance[now-1]>cost+1:
    heapq.heappush(queue,(cost+1,now-1));
    distance[now-1] = cost+1;
  
print(distance[k]);