from collections import deque
import copy
import sys;
input = sys.stdin.readline;
n,m = map(int,input().split());
arr = []
for _ in range(n):
  arr.append(list(map(int,input().rstrip())));
visited = [[False for _ in range(m)] for _ in range(n)];
d = [(1,0),(0,1),(-1,0),(0,-1)];
result = 1e9;
def bfs(x,y,visited):
  global result
  queue = deque()
  queue.append((1,x,y));
  while queue:
    cost,x,y = queue.popleft();
    visited[x][y] = True;
    if x==n-1 and y == m-1:
      result = min(cost,result);
    for i in range(4):
      dx,dy = d[i]
      next_x,next_y = x+dx,y+dy;
      if 0<=next_x<n and 0<=next_y<m:
        if visited[next_x][next_y] == False and arr[next_x][next_y] == 1:
          queue.append((cost+1,next_x,next_y));
          visited[next_x][next_y] = True;
bfs(0,0,visited);
print(result);