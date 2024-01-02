from collections import deque;
n,l,r = map(int,input().split());
data = [];
for i in range(n):
  data.append(list(map(int, input().split())));
result = 0;
dy = [1,0,0,-1]
dx = [0,1,-1,0];
def bfs(visited,x,y):
  queue = deque();
  queue.append((x,y));
  union_sum = 0;
  unions = []
  while queue:
    curx,cury = queue.popleft();
    visited[curx][cury] = True;
    union_sum += data[curx][cury];
    unions.append((curx,cury));
    for i in range(4):
      ny = cury + dy[i]
      nx = curx + dx[i]
      if ny < n and 0<=ny and 0<=nx and nx < n:
        if visited[nx][ny] == False and l<=abs(data[curx][cury] - data[nx][ny])<=r:
          queue.append((nx,ny));
          visited[nx][ny] = True;  
  union_number = int(union_sum/len(unions));
  for i,j in unions:
    data[i][j] = union_number;
  return len(unions);
while True:
  flag = 0;
  visited = [[False for _ in range(n)] for _ in range(n)];
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False:
        country = bfs(visited,i,j);
        if country>1:
          flag = 1;
  if flag == 0:
    break;
  else:
    result += 1;
print(result);