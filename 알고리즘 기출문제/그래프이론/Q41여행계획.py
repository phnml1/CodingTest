# p393
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,x);
  return parent[x];

def union_parent(parent,a,b):
  a = find_parent(parent, a);
  b = find_parent(parent, b);
  if a<b:
    parent[b] = a;
  else:
    parent[a] = b;

n,m = map(int,input().split());
arr = []
destinations = []
parent = [0] * (n+1);
graph = [[] for _ in range(n+1)]
result = True;
for i in range(n):
  data = list(map(int,input().split()));
  for j in range(n):
    if data[j] == 1:
      union_parent(parent,i+1,j+1)
destinations = list(map(int,input().split()))

for i in range(m-1):
  if find_parent[i] != find_parent[i+1]:
    result = False
# 내 풀이
# for i in range(n):
#   for j in range(n):
#     if arr[i][j] == 1:
#       graph[i+1].append(j+1);
      
# start = destinations[0];
# visited = [False for _ in range(n+1)];
# visited[start] = True
# q = deque()
# q.append(start);
# while q:
#   cur_node = q.popleft();  
#   for node in graph[cur_node]:
#     if visited[node] == False:
#       q.append(node);
#       visited[node] = True;
# for dest in destinations:
#   if visited[dest] == False:
#     result = False;
#     break;

if result:
  print('YES');
else:
  print('NO');