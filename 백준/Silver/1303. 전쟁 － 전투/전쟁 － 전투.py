from collections import deque
import sys;
input = sys.stdin.readline;
n,m = map(int,input().split());
arr = []
for _ in range(m):
  arr.append(list(input().rstrip()));
visited = [[False for _ in range(n)] for _ in range(m)];
b = 0;
w = 0;
d = [(1,0),(0,1),(-1,0),(0,-1)];
def count_soldier(i,j,visited):
  queue = deque();
  queue.append((i,j));
  count = 0;
  while queue:
    x,y = queue.popleft();
    visited[x][y] = True;
    count += 1;
    for i in range(4):
      dx,dy = d[i];
      next_x = x + dx;
      next_y = y + dy;
      if 0<=next_x<m and 0<=next_y<n and arr[x][y] == arr[next_x][next_y]:
        if visited[next_x][next_y] == False:
          queue.append((next_x,next_y));
          visited[next_x][next_y] = True;
  return count; 
for i in range(m):
  for j in range(n):
    if visited[i][j] == False:
      cnt = count_soldier(i,j,visited);
      if arr[i][j] == 'W':
        w+=cnt**2;
      else:
        b+=cnt**2;
print(w,b);
