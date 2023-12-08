import sys;
import heapq;
input = sys.stdin.readline
n = int(input());
m = int(input());
graph = [[] for _ in range(n+1)];
for i in range(m):
  c1,c2,cost = map(int, input().split());
  graph[c1].append([c2,cost]);
INF = 1e9;
for i in range(1,n+1):
  q = []
  costs = [INF for _ in range(n+1)]
  heapq.heappush(q,(0,i));
  costs[i] = 0;
  while q:
    cost,v = heapq.heappop(q);
    if cost>costs[v]:
      continue;
    for a in graph[v]:
      cur_cost = cost + a[1];
      if cur_cost < costs[a[0]]:
        heapq.heappush(q,(cur_cost,a[0]));
        costs[a[0]] = cur_cost;
  for j in range(1,n+1):
    if costs[j] == INF:
      print(0, end= ' ');
    else:
      print(costs[j], end=' ');
  print();
    