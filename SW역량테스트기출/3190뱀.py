from collections import deque
import sys
input = sys.stdin.readline
n = int(input());
k = int(input());
board = [[0 for _ in range(n)]for _ in range(n)];
direction = [(0,1),(1,0),(0,-1),(-1,0)];
for _ in range(k):
  x,y = map(int,input().split());
  board[x-1][y-1] = 1;
l = int(input());
turns = [];
bamn = deque();
bamn.append((0,0));
for i in range(l):
  t,dir = input().split();
  turns.append((int(t),dir));
time = 0;
dir = 0;
i = 0;
t,turndir = turns[i];
while True:
  time += 1;
  x,y = bamn[-1];
  if t == time:
    if turndir == 'L':
      dir = dir-1;
      if dir == -1:
        dir = 3;
    if turndir == 'D':
      dir = dir + 1;
      if dir == 4:
        dir  = 0;
    if i+1<len(turns):
      i = i+1;
      t,turndir = turns[i];
  plusx,plusy = direction[dir]
  next_x,next_y = x + plusx, y + plusy;
  if 0<=next_x<n and 0<=next_y<n and board[next_x][next_y] != 2:
    if board[next_x][next_y] == 0:
      bamn.append((next_x,next_y));
      px,py = bamn.popleft();
      board[px][py] = 0
      board[next_x][next_y] = 2;
    else:
      bamn.append((next_x,next_y));
      board[next_x][next_y] = 2;
  else:
    time += 1;
    break;
print(time);
  