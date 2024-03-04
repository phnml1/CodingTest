from collections import defaultdict
import copy


n,m = map(int,input().split());
arr = []
cctvs = [];
dir = [[-1,0],[0,1],[1,0],[0,-1]]
result = 1e9;
mode = [[],[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[0,3]],[[0,1,2],[0,1,3],[1,2,3],[0,2,3]],[[0,1,2,3]]];
for i in range(n):
  newarr = list(map(int,input().split()));
  for j in range(m):
    if newarr[j] != 0 and newarr[j]!=6:
      cctvs.append([newarr[j],i,j]);
  arr.append(newarr);
def fill(arr,mode,x,y):
  for i in mode:
    nx = x;
    ny = y;
    while True:
      nx += dir[i][0];
      ny += dir[i][1];
      if nx<0 or ny<0 or nx>=n or ny>=m:
        break;
      if arr[nx][ny] == 6:
        break;
      elif arr[nx][ny] == 0:
        arr[nx][ny] = -1;
def dfs(depth,arr):
  global result;
  if depth == len(cctvs):
    count = 0;
    for i in range(n):
      count += arr[i].count(0);
    result = min(result,count);
    return;
  temp = copy.deepcopy(arr);
  cctv_num,x,y = cctvs[depth];
  for i in mode[cctv_num]:
    fill(temp,i,x,y);
    dfs(depth+1,temp);
    temp = copy.deepcopy(arr);
dfs(0,arr);
print(result);