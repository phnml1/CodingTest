r,c,t = map(int,input().split());
arr = [];
dusts = [];
airs = []
dir = [[1,0],[0,1],[-1,0],[0,-1]];
for i in range(r):
  temp = list(map(int,input().split()));
  for j in range(c):
    if temp[j] != 0:
      if temp[j] != -1:
        dusts.append((i,j));
      else:
        airs.append((i,j));
  arr.append(temp);
def air_up():
  step = [[0,1],[-1,0],[0,-1],[1,0]];
  direct = 0;
  x,y = airs[0];
  up,y = x,1;
  previous = 0
  while True:
    nx,ny = x + step[direct][0],y+step[direct][1];
    if x==up and y == 0:
      break
    if nx<0 or nx>=r or ny<0 or ny>=c:
      direct += 1;
      continue
    arr[x][y],previous = previous,arr[x][y]
    x,y = nx,ny;
  return
def air_down():
  step = [[0,1],[1,0],[0,-1],[-1,0]];
  direct = 0;
  x,y = airs[1]
  down,y = x,1;
  previous = 0
  while True:
    nx,ny = x + step[direct][0],y+step[direct][1];
    if x==down and y == 0:
      break
    if nx<0 or nx>=r or ny<0 or ny>=c:
      direct += 1;
      continue
    arr[x][y],previous = previous,arr[x][y]
    x,y = nx,ny;
  return
def dust_diffusiton():
  step = [[-1,0],[1,0],[0,-1],[0,1]];
  diffustion = [[0] * c for _ in range(r)];
  for i in range(r):
    for j in range(c):
      if not (arr[i][j] == 0 or arr[i][j] == -1):
        turn = 0
        for dx,dy in step:
          nx,ny = i+dx,j+dy;
          if 0<=nx<r and 0<=ny<c and (nx,ny) not in airs:
            turn += 1;
            diffustion[nx][ny] += arr[i][j] // 5
        arr[i][j] = arr[i][j] - (arr[i][j] // 5 *turn);
  for i in range(r):
    for j in range(c):
      arr[i][j] += diffustion[i][j];
for _ in range(t):
  dust_diffusiton();
  air_up();
  air_down();
ans = 0
for i in range(r):
  for j in range(c):
    if arr[i][j] > 0:
      ans += arr[i][j]
      
print(ans);
