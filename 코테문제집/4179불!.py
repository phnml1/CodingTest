from collections import deque


r,c = map(int,input().split());
arr = []
fire = deque();
queue = deque();

visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]
for i in range(r):
  st = input();
  for j in range(c):
    if st[j] == 'J':
      queue.append((i,j));
      visited_j[i][j] = 1;
    if st[j] == 'F':
      fire.append((i,j))
      visited_f[i][j] = 1;
  new_arr = list(st)    
  arr.append(new_arr);
dir = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs():
  while fire:
    x,y = fire.popleft();
    for i in range(4):
      nx,ny = x+dir[i][0], y+dir[i][1];
      if 0<=nx<r and 0<=ny<c:
        if arr[nx][ny] != '#' and visited_f[nx][ny]==0:
            visited_f[nx][ny] = visited_f[x][y] + 1;
            fire.append((nx,ny));
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx,ny = x + dir[i][0], y + dir[i][1];
      if 0<=nx<r and 0<=ny<c:
        if not visited_j[nx][ny] and arr[nx][ny] != '#':
          if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:  
            visited_j[nx][ny] = visited_j[x][y] + 1;
            queue.append((nx,ny))
      else:
        return visited_j[x][y];
  return 'IMPOSSIBLE'

print(bfs());