import sys

input = sys.stdin.readline;
r,c = map(int,input().split());
arr = [];
dir = [(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(r):
  arr.append(list(input().rstrip()));
result = 0;
visited = [False for x in range(26)];
def dfs(cur_r,cur_c, visited,depth):
  global result
  result = max(result, depth);
  n = arr[cur_r][cur_c];
  visited[ord(n)-65] = True;
  check = 0;
  for i in range(4):
    dr,dc =  dir[i];
    next_r,next_c = cur_r+dr,cur_c+dc;
    if 0<=next_r<r and 0<=next_c<c:
      n = arr[next_r][next_c];
      if visited[ord(n)-65] == False:
        check += 1;
        dfs(next_r,next_c,visited,depth+1);
        visited[ord(n) - 65] = False;
  
  
dfs(0,0,visited,1);
print(result);