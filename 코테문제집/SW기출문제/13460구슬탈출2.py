from collections import deque
import sys
input = sys.stdin.readline;
n,m = map(int,input().split());
r,b = (),();
dir = [[1,0],[-1,0],[0,1],[0,-1]];
arr = []
for i in range(n):
  str = list(input());
  for j in range(len(str)):
    if str[j] == 'R':
      r = (i,j);
    if str[j] == 'B':
      b = (i,j)
  arr.append(str);
def bfs(r,b):
  queue = deque();
  queue.append((0,r,b));
  rx,ry = r;
  bx,by = b;
  visited = [] # 방문여부를 판단하기 위한 리스트
  visited.append((rx, ry, bx, by))
  while queue:
    count,r,b = queue.popleft();
    rx,ry = r;
    bx,by = b;
    if arr[rx][ry] == 'O':
      print(count);
      return;
    ncount = count+1
    for i in range(4):
      dx,dy = dir[i][0],dir[i][1];
      nrx,nry = rx,ry
      while True:
        nrx += dx;
        nry += dy;
        if arr[nrx][nry] == '#':
          nrx -= dx;
          nry -= dy;
          break;
        if arr[nrx][nry] == 'O':
          break;
      nbx,nby = bx,by
      while True:
        nbx +=  dx;
        nby +=  dy;
        if arr[nbx][nby] == '#':
          nbx -= dx;
          nby -= dy;
          break;
        if arr[nbx][nby] == 'O':
          nbx,nby = -1,-1;
          break;
      if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
        if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
          nrx -= dx
          nry -= dy
        else:
          nbx -= dx
          nby -= dy
      if nbx !=-1 and nby != -1 and ncount<=10 and (nrx,nry,nbx,nby) not in visited:
        queue.append((ncount,(nrx,nry),(nbx,nby)));
        visited.append((nrx,nry,nbx,nby));
  print(-1);
bfs(r,b)