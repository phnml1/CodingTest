import heapq


dir = [(1,0),(-1,0),(0,1),(0,-1)]
results = []
while True:
  p = int(input());
  if p == 0:
    break;
  arr = []
  for _ in range(p):
    arr.append(list(map(int,input().split())));
  q = []
  # 앞으로 이렇게 하자
  visited = [[1e9] *(p+1) for _ in range(p+1)]
  heapq.heappush(q,(arr[0][0],0,0));
  while q:
    cost,x,y = heapq.heappop(q);
    if x==p-1 and y==p-1:
      results.append(cost);
      break;
    for i in range(4):
      px,py = dir[i];
      next_x,next_y = x+px,y+py;
      if 0<=next_x<p and 0<=next_y<p:
        next_cost = cost + arr[next_x][next_y];
        if visited[next_x][next_y]==1e9 or next_cost < visited[next_x][next_y]:
          visited[next_x][next_y] = next_cost;
          heapq.heappush(q,(cost+arr[next_x][next_y],next_x,next_y))
for i in range(len(results)):
  print('Problem '+str(i+1)+': '+str(results[i]));