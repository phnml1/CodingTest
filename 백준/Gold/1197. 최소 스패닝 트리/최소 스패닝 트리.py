import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    p1 = find_parent(parent, a)
    p2 = find_parent(parent, b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

input = sys.stdin.readline
v, e = map(int, input().split())
edges = []
parent = [i for i in range(v + 1)];

for i in range(e):
    v1, v2, cost = map(int, input().split())
    edges.append((cost, v1, v2))

edges.sort()
result = 0

for edge in edges:
    cost, v1, v2 = edge
    if find_parent(parent, v1) != find_parent(parent, v2):
        union(parent, v1, v2)
        result += cost

print(result)