n = int(input());
k = int(input());
arr = [0 for _ in range(n+1) for _ in range(n+1)];
directioninfo = [];
for i in range(k):
  n1,n2 = map(int,input().split());
  arr[n1][n2] = 1;
l = int(input());
for i in range(l):
  x,c = input().split();
  directioninfo.append((int(x),c));
# 동,남,서,북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
  if c == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x,y = 1,1; # 뱀의 머리위치
  arr[x][y] = 2; # 뱀이 존재할때는 2로표시
  direction = 0; # 처음에는 동쪽을 보고 있음
  time = 0; #경과 시간(초)
  index = 0 #다음에 회전할 정보
  q = [(x,y)] #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  while True:
    nx = x+dx[direction];
    ny = y+dy[direction];
    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1<=nx and nx<=n and 1<=ny and ny<=n and arr[nx][ny] != 2:
      # 사과가 없다면 이동 후에 꼬리 제거
      if arr[nx][ny] == 0:
        arr[nx][ny] = 2
        q.append((nx,ny));
        px,py = q.pop(0)
        arr[px][py] = 0
      if arr[nx][ny] == 1:
        arr[nx][ny] = 2;
        q.append((nx,ny));
    else:
      time += 1
      break;
    x,y = nx,ny
    time += 1
    if index<l and time == directioninfo[index][0]:
      direction = turn(direction,directioninfo[index][1])
      index += 1
  return time

print(simulate());