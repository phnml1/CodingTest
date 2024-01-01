# from collections import deque
# from itertools import *
# import copy
# n,m = map(int,input().split());
# arr = []
# blanks,wall_num = [],0;
# for i in range(n):
#   arr.append(list(map(int,input().split())));
# for i in range(n):
#   for j in range(m):
#     if arr[i][j] == 0:
#       blanks.append((i,j));
#     if arr[i][j] == 1:
#       wall_num += 1
# p_walls = list(combinations(blanks,3));

# def bfs(i,j,testarr):
#     dr = [1,-1,0,0]
#     dc = [0,0,1,-1]
#     count = 0
#     queue = deque()
#     queue.append((i,j));
#     testarr[i][j] = 3
#     while queue:
#         cur_r,cur_c = queue.popleft()
#         count +=1;
#         for a in range(4):
#             if 0<=cur_r+dr[a]<r and 0<=cur_c+dc[a]<c:
#                 if testarr[cur_r+dr[a]][cur_c+dc[a]] == 0 or testarr[cur_r+dr[a]][cur_c+dc[a]] == 2:
#                     testarr[cur_r + dr[a]][cur_c+dc[a]] = 3;
#                     queue.append((cur_r+dr[a],cur_c+dc[a]));
#     return count;
  
# for pwall in p_walls:
#     testarr = copy.deepcopy(arr);
#     cur_result = 0;
#     for wall in pwall:
#         testarr[wall[0]][wall[1]] = 1;
#     for i in range(n):
#         for j in range(m):
#             if testarr[i][j] == 2:
#                 cur_result += bfs(i,j,testarr);
#     result = min(result,cur_result);

#책에서의 dfs풀이
n,m = map(int,input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] #벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  data.append(list(map(int,input().split())));
  
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    #상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < n and ny>=0 and ny<m:
      if temp[nx][ny] == 0:
        # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
        temp[nx][ny] = 2
        virus(nx,ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드       
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if [i][j] == 0:
        score += 1

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
    result = max(result,get_score());
    return
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1
dfs(0)
print(result)
   