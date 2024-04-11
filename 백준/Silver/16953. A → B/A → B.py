import sys;
input = sys.stdin.readline;
a,b = map(int,input().split());
result = 1e9;
def dfs(num,cnt):
  global result;
  if num>b:
    return;
  if num == b:
    result = min(result,cnt);
    return;
  dfs(num*2,cnt+1);
  dfs(int(str(num)+'1'),cnt+1)
dfs(a,1);
if result != 1e9:
  print(result);
else:
  print(-1);