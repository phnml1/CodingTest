from collections import deque;
# p341
n,m,k,x = map(int, input().split());
result = []
graph = [[] for _ in range(n+1)];
for i in range(m):
  i1,i2 = map(int,input().split());
  graph[i1].append(i2);
distance = [-1 for _ in range(n+1)];
distance[x] = 0;
q = deque()
q.append(x);
visited = [False for _ in range(n+1)];
while q:
  cur_v = q.popleft();
  visited[cur_v] = True;
  for next_v in graph[cur_v]:
    if distance[next_v] == -1:
      distance[next_v] = distance[cur_v] + 1;
      q.append(next_v);
result.sort();
check = False
for i in range(n+1):
  if distance[i] == k:
    print(i);
    check = True
if check==False:
  print(-1);

