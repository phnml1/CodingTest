import heapq;
import sys;

input = sys.stdin.readline;
INF = int(1e9);
n,m,c = map(int,input().split());
graph = [[] for i in range(n+1)];
costs = [10000000 for i in range(n+1)];
for i in range(m):
  x,y,z = map(int,input().split());
  graph[x].append([y,z]);
q = []
heapq.heappush(q,(c,0));
costs[c] = 0
while q:
  v, cost = heapq.heappop(q);
  if costs[v]>=cost:
    for i in graph[v]:
      costs[i[0]] = cost + i[1];
      heapq.heappush(q,(i[0],cost + i[1]));
number = 0
maxcost = 0
print(costs)
for i in range(1,n+1):
  if costs[i] <10000000:
    maxcost = max(costs[i],maxcost);
    number += 1;
print(number-1,maxcost)

    
  