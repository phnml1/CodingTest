# p 401 
from collections import deque

for tc in range(int(input())):
  # 노드의 개수 입력 받기
  n = int(input());
  # 모든 노드에 대한 진입 차수는 0으로 초기화
  indegree = [0] * (n+1);
  graph = [[False]*(n+1) for i in range(n+1)];
  data = list(map(int,input().split()));
  
  for i in range(n):
    for j in range(i+1,n):
      graph[data[i]][data[j]] = True
      indegree[data[j]] += 1
  m = int(input())
  for i in range(m):
    a,b = map(int,input().split())
    if graph[a][b]:
      graph[a][b] = False
      graph[b][a] = True
      indegree[a] += 1
      indegree[b] -= 1
    else:
      graph[a][b] = True
      graph[b][a] = False
      indegree[b] += 1
      indegree[a] -= 1
    
    result = []
    q = deque()
    
    for i in range(1,n+1):
      if indegree[i] == 0:
        q.append(i);
    certain = True #위상 정렬 결과가 오직하나인지의 여부
    cycle = False #사이클여부
    #정확히 노드의 개수만큼 반복
    for i in range(n):
      #큐가 비어있다면 사이클
      if len(q) == 0:
        cycle=True
        break
      if len(q) > 1:
        certain = False
        break
      now = q.popleft()
      result.append(now)
      
      for j in range(1,n+1):
        if graph[now][j]:
          indegree[j] -= 1
          if indegree[j] == 0:
            q.append(j);
  if cycle:
    print('IMPOSSIBLE')
  elif certain==False:
    print('?')
  else:
    for i in result:
      print(i, end = ' ')
    print();