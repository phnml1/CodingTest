import sys
from collections import deque
input = sys.stdin.readline
n = int(input());
arr = []
moves = [(-1,-0),(0,-1),(0,1),(1,0)];
INF = 1e9;
size = 2;
cur_y,cur_x = 0,0;
for i in range(n):
  arr.append(list(map(int,input().split())));

def bfs():
  visited = [[-1 for _ in range(n)] for _ in range(n)]
  queue = deque()
  queue.append((cur_y,cur_x));
  visited[cur_y][cur_x] = 0;
  while queue:
    y,x = queue.popleft();
    for move in moves:
      dy,dx = move
      nx = x+dx;
      ny = y+dy;
      if 0<=nx and nx<n and 0<=ny and ny<n:
        if arr[ny][nx] <= size and visited[ny][nx] == -1:
          visited[ny][nx] = visited[y][x] +1;
          queue.append((ny,nx));
  return visited;

def solve(visited):
  y,x = 0,0
  min_distance = INF;
  for i in range(n):
    for j in range(n):
      if visited[i][j] != -1 and 1<=arr[i][j]<size:
        if visited[i][j] < min_distance:
          min_distance = visited[i][j];
          y,x = i,j
  if min_distance == INF:
    return False
  else: 
    return y,x,min_distance

for i in range(n):
  for j in range(n):
    if arr[i][j] == 9:
      cur_y,cur_x = i,j;
      arr[i][j] = 0;

answer = 0;
food = 0;
while 1:
  result = solve(bfs());
  if not result:
    print(answer)
    break
  else:
    cur_y,cur_x = result[0],result[1]
    answer += result[2]
    arr[cur_y][cur_x] = 0; 
    food += 1
  if food >= size:
    size += 1
    food = 0