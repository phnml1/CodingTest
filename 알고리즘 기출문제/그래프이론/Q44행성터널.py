# p 400
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x]);
  return parent[x];

def union(parent,x,y):
  a = parent[x]
  b = parent[y]
  if a<b:
    parent[b] = a;
  else:
    parent[a] = b;  

n = int(input());
xarr,yarr,zarr = [],[],[];
edges = []
parent = [0] * (n+1);
result = 0
for i in range(n+1):
  parent[i] = i
for i in range(n):
  x,y,z = map(int,input().split());
  xarr.append(x);
  yarr.append(y);
  zarr.append(z);
xarr.sort();
yarr.sort();
zarr.sort();
for i in range(n-1):
  edges.append((xarr[i+1] - xarr[i],i,i+1));
  edges.append((yarr[i+1] - yarr[i],i,i+1));
  edges.append((zarr[i+1] - zarr[i],i,i+1));
edges.sort();
for edge in edges:
  cost,a,b = edge;
  if find_parent(parent,a) != find_parent(parent,b):
    union(parent,a,b)
    result += cost;
print(result);
