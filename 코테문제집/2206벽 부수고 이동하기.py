from collections import deque


n,m = map(int,input().split());
arr = []
dir = [(1,0),(0,1),(-1,0),(0,-1)];
for _ in range(n):
  str = list(input())
  str = list(map(int,str))
  arr.append(str);
move = [[[0,0] for _ in range(m)] for _ in range(n)];
move[0][0][0] = 1;
def bfs(x,y,z):
  queue = deque([(0,0,0)])
  while queue:
    x,y,z = queue.popleft();
    if x == n-1 and y == m-1:
      return move[x][y][z];
    for i in range(4):
      dirx,diry = dir[i]
      nx = x + dirx;
      ny = y + diry;
      if 0<=nx<n and 0<=ny<m:
        if arr[nx][ny] == 1 and z == 0:
          move[nx][ny][1] = move[x][y][0] + 1
          queue.append((nx,ny,1));
        elif arr[nx][ny] == 0 and move[nx][ny][z] == 0:
          move[nx][ny][z] = move[x][y][z] + 1
          queue.append((nx,ny,z));
  return -1

print(bfs(0,0,0));