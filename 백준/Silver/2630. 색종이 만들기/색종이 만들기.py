n = int(input());
arr = []
ans_0,ans_1 = 0,0;
for i in range(n):
  arr.append(list(map(int,input().split())));
def dfs(x,y,n):
  global ans_0,ans_1;
  color = arr[x][y];
  for i in range(x,x+n):
    for j in range(y,y+n):
      if color != arr[i][j]:
        dfs(x,y,n//2);
        dfs(x,y+n//2,n//2);
        dfs(x+n//2,y,n//2);
        dfs(x+n//2,y+n//2,n//2);
        return;
  if color == 0:
    ans_0 += 1;
  if color == 1:
    ans_1 += 1;
  
  return;
dfs(0,0,n);
print(ans_0);
print(ans_1);
