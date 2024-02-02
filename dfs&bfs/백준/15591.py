from collections import defaultdict, deque
import sys
input = sys.stdin.readline
N,Q = map(int,input().split());
graph = defaultdict(list);
results = []
for i in range(N-1):
  p,q,r = map(int,input().split());
  graph[p].append((r,q));
  graph[q].append((r,p));
for i in range(Q):
  k,v = map(int,input().split());
  queue = deque();
  visited = [False] * (N+1);
  visited[v] = True;
  count = 0;
  queue.append((float('inf'),v));
  while queue:
    r,node = queue.popleft();
    for cur_cost,cur_node in graph[node]:
      if visited[cur_node] == False:
        next_cost = min(r,cur_cost);
        if next_cost>=k:
            visited[cur_node] = True;
            queue.append((next_cost,cur_node));
            count += 1;
  print(count);