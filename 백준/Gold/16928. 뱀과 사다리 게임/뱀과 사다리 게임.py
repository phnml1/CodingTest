import sys
from collections import defaultdict, deque
input = sys.stdin.readline;
n,m = map(int,input().split());
result = 0;
costs = [1e9 for _ in range(101)];
path = defaultdict(int);
dir = [1,2,3,4,5,6];
for _ in range(n):
  s,t = map(int,input().split());
  path[s]=t;
for _ in range(m):
  s,t = map(int,input().split());
  path[s]=t;
start = 1;
queue = deque();
queue.append((0,start));
while queue:
  cur_cost, cur_node = queue.popleft();
  for i in range(6):
    next_node = cur_node + dir[i];
    next_cost = cur_cost + 1;
    if 1> next_node or next_node> 100:
      continue;
    if path[next_node]!=0:
      next_node = path[next_node];
    if next_cost < costs[next_node]:
      costs[next_node] = next_cost;
      queue.append((next_cost,next_node));
print(costs[100]);