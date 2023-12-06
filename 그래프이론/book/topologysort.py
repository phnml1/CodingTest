from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v,e = map(int,input().split());
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1);
# 각 노드에 연결된 간선 정보를 담기 위한 그래프 초기화
graph = [[] for i in range(v+1)];

# 방향 그래프의 모든 간선 정보입력받기
for _ in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  # 진입차수를 1증가
  indegree[b] += 1
  
# 위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용
  
  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)
    
  while q:
    now = q.popleft()
    result.append(now)
    
    for i in graph[now]:
      indegree[i] -=1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end= ' ');

topology_sort();