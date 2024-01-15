# p388
INF = 1e9;
n,m = map(int,input().split());
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
count = [0 for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split());
  graph[a][b] = 1;
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j]);
      
for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] != INF:
      count[i] += 1;
      count[j] += 1;
result = 0

for i in range(1,n+1):
  if count[i] == n-1:
    result += 1;
print(result);
