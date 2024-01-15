def find_parent(parent,a):
  if parent[a] != a:
    parent[a] = find_parent(parent,parent[a]);
  return parent[a];

def union_parent(parent,a,b):
  a = find_parent(parent,a);
  b = find_parent(parent,b);
  if a<b:
    parent[b] = a;
  else:
    parent[a] = b;
# p 399
result = 0
n,m = map(int,input().split());
edges = []
for i in range(m):
  x,y,z = map(int,input().split());
  edges.append((z,x,y));
parent = [i for i in range(n+1)]
edges.sort();
for edge in edges:
  cost,x,y = edge;
  if find_parent(parent,x) != find_parent(parent,y):
    union_parent(parent,x,y);
  else:
    result += cost;
print(result);