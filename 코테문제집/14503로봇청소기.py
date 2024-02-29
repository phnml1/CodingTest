import sys
input = sys.stdin.readline;
n,m = map(int,input().split());
r,c,d = map(int,input().split());
arr = []
for _ in range(n):
  arr.append(list(map(int,input().split())));
dirs = [[-1,0],[0,1],[1,0],[0,-1]];
result = 0;
def dfs(x,y,dir):
  global result;
  if arr[x][y] ==0:
    arr[x][y] = 2;
    result += 1;
  for _ in range(4):  
    dir = dir-1
    if dir == -1:
      dir = 3;
    nx = x + dirs[dir][0];
    ny = y + dirs[dir][1];
    if 0<=nx<n and 0<=ny<m:
      if arr[nx][ny] == 0:
        dfs(nx,ny,dir);
        return;
  nx = x-dirs[dir][0];
  ny = y-dirs[dir][1];
  if 0<=nx<n and 0<=ny<m:
    if arr[nx][ny] == 1:
      return;
    else:
      dfs(nx,ny,dir);
dfs(r,c,d)
print(result);    
    