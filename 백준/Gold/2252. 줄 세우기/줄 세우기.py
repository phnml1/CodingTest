from collections import deque
import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
graph = [[] for _ in range(n+1)];
indegree = [0 for _ in range(n+1)];
result = []
for _ in range(m):
  a,b = map(int,input().split());
  graph[a].append(b);
  indegree[b] += 1;
queue = deque();
for i in range(1,n+1):
  if indegree[i] == 0:
    queue.append(i);
while queue:
  now = queue.popleft();
  result.append(now);
  for node in graph[now]:
    indegree[node] -= 1;
    if indegree[node] == 0:
      queue.append(node);
for a in result:
  print(a, end = ' ');
