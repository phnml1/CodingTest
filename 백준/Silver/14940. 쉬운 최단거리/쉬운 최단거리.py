import sys;
from collections import deque;

input = sys.stdin.readline;

n,m = map(int,input().split());
arr = [];
dir = [(1,0),(0,1),(-1,0),(0,-1)];
queue = deque();
costs = [[1e9 for _ in range(m)] for _ in range(n)];

for i in range(n):
  cur = list(map(int,input().split()));
  if 2 in cur:
    j = cur.index(2);
    queue.append((0,i,j));
    costs[i][j] = 0;
  arr.append(cur);


while queue:
  dis, r, c = queue.popleft();
  for i in range(4):
    dr,dc = dir[i];
    next_r, next_c = r + dr, c + dc;
    if 0<=next_r<n and 0<=next_c<m:
      if arr[next_r][next_c] == 1 and costs[next_r][next_c] > dis+1 :
        costs[next_r][next_c] = dis + 1;
        queue.append((dis+1,next_r,next_c));

for i in range(n):
  for j in range(m):
    if costs[i][j] == 1e9 and arr[i][j] == 0:
      print(0, end = ' ');
    elif costs[i][j] == 1e9 and arr[i][j] == 1:
        print(-1,end = ' ');
    else: 
      print(costs[i][j],end = ' ');
  print();