# 경로 압축 기법
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
  a = find_parent(parent, a);
  b = find_parent(parent, b);
  if a< b:
    parent[b] = a;
  else:
    parent[a] = b;

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int, input().split());
parent = [0] * (v+1);

for i in range(v+1):
  parent[i] = i;
  

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0
# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
  a,b,cost = map(int,input().split());
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost,a,b));
edges.sort();

for edge in edges:
  cost,a,b = edge;
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b);
    result += cost;
    last = cost;

print(result-last);
  