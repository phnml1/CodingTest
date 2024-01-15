# p392
import heapq
n,m = map(int,input().split());
graph = [[] for _ in range(n+1)];
results =  [];
result_number,result_dis,result_count = 0,0,0
for i in range(m):
  a,b = map(int,input().split());
  graph[a].append(b);
  graph[b].append(a);
def dikstra(end):
  visited = [False for _ in range(n+1)];
  q = []
  heapq.heappush(q,(0,1));
  while q:
    dis,node = heapq.heappop(q);
    if node == end:
      return dis;
    for cur_node in graph[node]:
      if visited[cur_node] == False:
        cur_dis = dis + 1;
        heapq.heappush(q,(cur_dis,cur_node));
        visited[cur_node] = True;
  return 0;
for i in range(2,n+1):
  result = dikstra(i);
  node = i;
  results.append([result,node]);
results.sort(key = lambda x: (-x[0],x[1]));
result_dis = results[0][0];
result_number = results[0][1];
for result in results:
  if result[0] == result_dis:
    result_count += 1;
print(result_number,result_dis,result_count);