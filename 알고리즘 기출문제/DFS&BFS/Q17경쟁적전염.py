from collections import deque;
n,k = map(int,input().split());
arr = [];
viruses = [];
for i in range(n):
  arr.append(list(map(int,input().split())));
s,x,y = map(int,input().split());

for i in range(n):
  for j in range(n):
    if arr[i][j] != 0:
      viruses.append((arr[i][j],i,j));
viruses.sort();

dy = [1,0,0,-1]
dx = [0,1,-1,0]
cur_time = 0
queue = deque();
for virus in viruses:
  kind,i,j = virus;
  queue.append((cur_time,kind,i,j));
while queue: 
  cur_time,cur_kind,i,j = queue.popleft();
  if cur_time > s:
    break;
  if arr[i][j] == 0:
    arr[i][j] = cur_kind;
  for a in range(4):
    ny = dy[a] + i;
    nx = dx[a] + j;
    if 0<=ny and ny<n and 0<=nx and nx<n:
      if arr[ny][nx] == 0:
        queue.append((cur_time+1,cur_kind,ny,nx));
print(arr)
print(arr[x-1][y-1]);
      
    
  
  