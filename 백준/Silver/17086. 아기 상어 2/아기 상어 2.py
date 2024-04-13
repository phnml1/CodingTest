from collections import deque
import sys;
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = [];
result = 0;
d = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
for _ in range(n):
  arr.append(list(map(int,input().split())));
def bfs(x,y):
  queue = deque();
  queue.append((0,x,y));
  visited = [[False for _ in range(m)]for _ in range(n)]
  while queue:
    cost,x,y = queue.popleft();
    visited[x][y] = True;
    if arr[x][y] == 1:
      return cost;
    for dx,dy in d:
      next_x,next_y = x+dx,y+dy;
      if 0<=next_x<n and 0<=next_y<m and not visited[next_x][next_y]:
        queue.append((cost+1,next_x,next_y))
        visited[next_x][next_y] = True;
for i in range(n):
  for j in range(m):
    if arr[i][j] == 0:
      result = max(result,bfs(i,j));
print(result);
