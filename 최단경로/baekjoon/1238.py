import sys;
import heapq;

input = sys.stdin.readline;
INF = 1e9;
n,m,x= map(int,input().split());
graph = [[] for _ in range(n+1)];
for _ in range(m):
  num1,num2,num3 = map(int,input().split());
  graph[num1].append([num2,num3]);
costs = [INF for _ in range(n+1)];
def dikstra(start,final):
  if final==start:
    return 0;
  q = [];
  costs = [INF for _ in range(n+1)];
  heapq.heappush(q,(0,start));
  while q:
    cost, v = heapq.heappop(q);
    if costs[v] < cost:
      continue
    for i in graph[v]:
      cur_cost = cost + i[1];
      if cur_cost<costs[i[0]]:
        heapq.heappush(q,(cur_cost,i[0]));
        costs[i[0]] = cur_cost;
  return costs[final];
result = 0;
for i in range(1,n+1):
  cur_res = dikstra(i,x) + dikstra(x,i);
  if cur_res<INF:
    result = max(result,cur_res);
print(result);

  
