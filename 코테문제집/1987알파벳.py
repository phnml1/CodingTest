#시간초과
# r,c = map(int,input().split());
# arr = [['']*c for _ in range(r)];
# for i in range(r):
#   a = input().rstrip();
#   for j in range(c):
#     arr[i][j] = a[j];
# dir = [(1,0),(0,1),(-1,0),(0,-1)];
# alphabets = [];
# visited = [[False] * (c+1) for _ in range(r+1)];
# result = 0 ;
# def dfs(alphabets,x,y,count):
#   global result;
#   alpha = alphabets.copy();
#   alpha.append(arr[x][y]);
#   result = max(result,count);
#   for i in range(4):
#     cur_x,cur_y = dir[i];
#     next_x,next_y = x+cur_x, y+cur_y;
#     if 0<=next_x<r and 0<=next_y<c:
#       if arr[next_x][next_y] not in alpha:
#         dfs(alpha,next_x,next_y,count+1);
# dfs(alphabets,0,0,1);
# print(result)
import sys
input=sys.stdin.readline

n, m=map(int,input().split())
board=[list(input().strip()) for i in range(n)]
visited=[0]*26
dx=[-1,0,1,0]
dy=[0,1,-0,-1]
maxcnt=0

def dfs(alphabet,x,y, cnt):
    global maxcnt
    alpha = alphabet.copy()
    alpha.append(board[x][y])
    maxcnt=max(cnt, maxcnt)
    if cnt==10:
      print(alpha);
    for i in range(4):
        nx, ny= x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[ord(board[nx][ny])-ord('A')]==0:
            visited[ord(board[nx][ny])-ord('A')]=1
            dfs(alpha,nx,ny,cnt+1)
            visited[ord(board[nx][ny])-ord('A')]=0

visited[ord(board[0][0])-ord('A')]=1
dfs([],0,0,1)
print(maxcnt) 
  