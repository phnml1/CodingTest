n = int(input());
graph = [0 for _ in range(n+1)];
result = []
for i in range(1,n+1):
  graph[i] = int(input());
def dfs(start,i,paths):
  global result
  if i not in paths:
    paths.append(i);
    if start == graph[i]:
      result += paths
      return;
    else:
      dfs(start,graph[i],paths);
for i in range(1,n+1):
  paths = [];
  if i not in result:
    if i == graph[i]:
      result.append(i)
    else:
      paths.append(i);
      dfs(i,graph[i],paths);
print(len(result))
result.sort()
for res in result:
  print(res);