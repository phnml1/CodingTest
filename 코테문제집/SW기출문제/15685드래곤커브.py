import sys
input = sys.stdin.readline;
dir = [[0,1],[-1,0],[0,-1],[1,0]];
graph =  [[0]*101 for _ in range(101)];
n = int(input());
answer = 0
for _ in range(n):
  x,y,d,g = map(int,input().split());
  graph[y][x] = 1;
  infos = []
  infos.append(d);
  for _ in range(g):  
    temp = []
    for i in range(len(infos)-1,-1,-1):
      cur_dir = (infos[i]+1)%4;
      
      temp.append(cur_dir);
    infos.extend(temp);
  for info in infos:
    dir_y = dir[info][0];
    dir_x = dir[info][1];
    x  = x+dir_x;
    y = y + dir_y;
    if x<0 or 100<x or y<0 or 100<y:
        continue;
    graph[y][x] = 1;
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1
print(answer);