from collections import deque
import sys;
input = sys.stdin.readline;
n,m,k = map(int,input().split());
arr = [[0 for _ in range(m)] for _ in range(n)];
for _ in range(k):
  r,c = map(int,input().split());
  arr[r-1][c-1] = 1;
visited = [[False for _ in range(m)] for _ in range(n)];
d = [(1,0),(0,1),(-1,0),(0,-1)];
result = 0;
def bfs(x,y,visited):
  global result
  queue = deque()
  queue.append((x,y));
  cnt = 0;
  while queue:
    x,y = queue.popleft();
    visited[x][y] = True;
    cnt += 1;
    for i in range(4):
      dx,dy = d[i]
      next_x,next_y = x+dx,y+dy;
      if 0<=next_x<n and 0<=next_y<m:
        if visited[next_x][next_y] == False and arr[next_x][next_y] == 1:
          queue.append((next_x,next_y));
          visited[next_x][next_y] = True;
  return cnt;
for i in range(n):
  for j in range(m):
    if visited[i][j] == False and arr[i][j]==1:
      result=max(result,bfs(i,j,visited));
print(result);