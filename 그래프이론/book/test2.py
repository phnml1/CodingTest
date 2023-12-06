def find_parent(parent,x):
  if parent[x] !=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x];
def union_parent(parent,n1,n2):
  p1 = find_parent(parent,n1);
  p2 = find_parent(parent,n2);
  if p1<p2:
    parent[n2] = p1;
  else:
    parent[n1] = p2;
n,m = map(int,input().split());
parent = [0] * (n+1);
for i in range(1,n+1):
  parent[i] = i;
arr = [] 
for i in range(m):
  kind,node1,node2 = map(int,input().split());
  arr.append((kind,node1,node2));
for i in arr:
  kind,node1,node2 = i;
  if kind==0:
    union_parent(parent,node1,node2);
  else:
    if find_parent(parent,node1) == find_parent(parent,node2):
      print('YES');
    else:
      print('NO');
