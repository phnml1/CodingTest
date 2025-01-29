import sys;
input = sys.stdin.readline;
n = int(input());

result = 0;
def dfs(row,visited):
  global result;
  if row == n:
    result += 1;
    return;
  for i in range(n):
    cur_r,cur_c = row,i;
    flag = False;
    for node in visited:
      a,b = node;
      if b==cur_c or a-b == cur_r-cur_c or a+b == cur_r+cur_c:
        flag = True;
        break;
    if flag:
      continue;
    visited.append((cur_r,cur_c));
    dfs(row+1,visited);
    visited.pop();
for i in range(n):        
  dfs(1,[(0,i)]);
print(result);