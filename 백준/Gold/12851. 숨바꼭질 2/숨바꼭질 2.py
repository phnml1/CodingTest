from collections import defaultdict
import sys;
import heapq;
input = sys.stdin.readline;
n,k = map(int,input().split());
case = 0;
visited = defaultdict(lambda: 1e9);
def bfs(visited):
  global case;
  visited[n] = 0;
  queue = []
  heapq.heappush(queue,(0,n));
  while queue:
    cost,num = heapq.heappop(queue);
    if cost < visited[num]:
      visited[num] = cost;
    if num == k:
      if cost < visited[k]:
        case = 1;
      if cost == visited[k]:
        case += 1;
    if cost<=visited[num] and 0<=num<k:
      heapq.heappush(queue,(cost+1,num+1));
      heapq.heappush(queue,(cost+1,num*2));
    if cost<=visited[num] and ((0<=num<k) or (k<num and num - k + cost<=visited[k])):
      heapq.heappush(queue,(cost+1,num-1));
bfs(visited);
print(visited[k]);
print(case);
