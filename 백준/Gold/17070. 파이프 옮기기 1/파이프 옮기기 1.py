import sys;
input = sys.stdin.readline;
n = int(input());
arr = []
result = 0;
for _ in range(n):
  arr.append(list(map(int,input().split())));
def dfs(x,y,state):
  global result;
  if x==n-1 and y==n-1:
    result += 1;
  if state == 0:
    if 0<=x<n and 0<=y+1<n:
      if arr[x][y+1] == 0:
        dfs(x,y+1,0)
    if 0<=x+1<n and 0<=y<n and 0<=x<n and 0<=y+1<n and 0<=x+1<n and 0<=y+1<n:
      if arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1] ==0:
        dfs(x+1,y+1,2);
  if state == 1:
    if 0<=x+1<n and 0<=y<n:
      if arr[x+1][y] == 0:
        dfs(x+1,y,1);
    if 0<=x+1<n and 0<=y<n and 0<=x<n and 0<=y+1<n and 0<=x+1<n and 0<=y+1<n:
      if arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1] ==0:
        dfs(x+1,y+1,2);
  if state == 2:
    if 0<=x+1<n and 0<=y<n:
      if arr[x+1][y] == 0:
        dfs(x+1,y,1);
    if 0<=x<n and 0<=y+1<n:
      if arr[x][y+1] == 0:
        dfs(x,y+1,0)  
    if 0<=x+1<n and 0<=y<n and 0<=x<n and 0<=y+1<n and 0<=x+1<n and 0<=y+1<n:
      if arr[x][y+1] == 0 and arr[x+1][y] == 0 and arr[x+1][y+1] ==0:
        dfs(x+1,y+1,2);
dfs(0,1,0);
print(result);