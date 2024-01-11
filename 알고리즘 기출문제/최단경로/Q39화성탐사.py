import heapq
t = int(input());
dx = [1,0,0,-1]
dy = [0,-1,1,0];
INF = 1e9
for _ in range(t):
  n = int(input());
  graph = [];
  for i in range(n):
    graph.append(list(map(int,input().split())));
  q = [];
  heapq.heappush(q,(graph[0][0],0,0));
  costs = {};
  while q:
    cur_cost,cur_x,cur_y = heapq.heappop(q);
    for i in range(4):
      newy = cur_y + dy[i]
      newx = cur_x + dx[i]
      if 0<=newy<n and 0<=newx<n and (newx,newy) not in costs:
        new_cost = cur_cost + graph[newx][newy];
        costs[(newx,newy)] = new_cost;
        heapq.heappush(q,(new_cost,newx,newy));
  print(costs[(n-1,n-1)])