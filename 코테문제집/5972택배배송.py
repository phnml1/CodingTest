import heapq

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)];
for _ in range(m):
  a_i,b_i,c_i = map(int,input().split());
  graph[a_i].append((c_i,b_i));
  graph[b_i].append((c_i,a_i));
start = 1;distances = [1e9 for _ in range(n+1)];
queue = []
heapq.heappush(queue,(0,1))
while queue:
  cost,node = heapq.heappop(queue);
  for a in graph[node]:
    new_cost,new_node = a;
    next_cost = new_cost + cost
    if distances[new_node]>next_cost:
      heapq.heappush(queue,(next_cost,new_node));
      distances[new_node] = next_cost;
print(distances[n]);