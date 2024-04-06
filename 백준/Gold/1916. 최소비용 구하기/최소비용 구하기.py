import heapq;
N = int(input());
M = int(input());
graph = [[] for _ in range(N+1)];
for _ in range(M):
  a,b,c = map(int,input().split());
  graph[a].append((c,b));
start,end = map(int,input().split());
queue = [];
costs = [1e9 for _ in range(N+1)];
costs[start] = 0
heapq.heappush(queue,(costs[start],start));
while queue:
  cur_cost, cur_node = heapq.heappop(queue);
  #이미 cur_node로 가는 최적의 경우를 구한 것
  if costs[cur_node]<cur_cost:
    continue;
  for c,b in graph[cur_node]:
    next_cost = cur_cost + c
    if next_cost<costs[b]:
      costs[b] = next_cost;
      heapq.heappush(queue,(next_cost, b));
print(costs[end]);
    