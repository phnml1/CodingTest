import sys
import heapq;
input = sys.stdin.readline;
v,e = map(int,input().split());
k = int(input());
INF = 1e9;
graph = [[] for _ in range(v+1)];
for _ in range(e):
  n1,n2,n3 = map(int,input().split());
  graph[n1].append([n2,n3]);
q = [];
costs = [INF for _ in range(v+1)];
costs[k] = 0;
heapq.heappush(q,(0,k));
while q:
  cost,node = heapq.heappop(q);
  if cost>costs[node]:
    continue;
  for i in graph[node]:
    cur_cost = i[1] + cost;
    if costs[i[0]]>cur_cost:
      costs[i[0]] = i[1] + cost;
      heapq.heappush(q,(i[1]+cost,i[0]));
for i in range(1,v+1):
  if costs[i]<INF:
    print(costs[i]);
  else:
    print('INF');