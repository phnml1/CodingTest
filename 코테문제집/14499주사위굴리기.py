n,m,x,y,k = map(int,input().split());
arr = []
orders = []
dir = [0,[0,1],[0,-1],[-1,0],[1,0]];
dice = [0,0,0,0,0,0];
for _ in range(n):
  arr.append(list(map(int,input().split())));
orders = list(map(int,input().split()));
  
  
for order in orders:
  nx = x + dir[order][0];
  ny = y + dir[order][1];
  if n<=nx or nx<0 or m<=ny or ny<0:
    continue;
  east,west,south,north,ceiling,floor = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5];
  if order == 1:
    dice[0], dice[1], dice[4], dice[5] = floor, ceiling, east, west
  elif order == 2:
    dice[0], dice[1], dice[4], dice[5] = ceiling, floor, west, east
  elif order == 3:
    dice[2], dice[3], dice[4], dice[5] = ceiling, floor, north, south
  elif order == 4:
    dice[2], dice[3], dice[4], dice[5] = floor, ceiling, south, north
  if arr[nx][ny] ==0:
    arr[nx][ny] = dice[5];
  else:
    dice[5] = arr[nx][ny];
    arr[nx][ny] = 0;
  x,y = nx,ny;
  print(dice[4]);
  