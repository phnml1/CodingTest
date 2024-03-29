n = int(input());
equal = list(input().rstrip());
ans = 0;
def operator(num1,oper,num2):
  if oper == '+':
    return num1 + num2;
  elif oper == '-':
    return num1 - num2;
  elif oper == '*':
    return num1 * num2;

def dfs(idx,target):
  global ans
  if idx == n-1:
    ans = max(ans,target);
    return;
  if idx +2 <n:
    dfs(idx+2,operator(target,equal[idx+1],equal[idx+2]))
  if idx + 4<n:
    dfs(idx+4,operator(target,equal[idx+1],(operator(equal[idx+2],equal[idx+3],equal[idx+4]))))
for i in range(0,len(equal),2):
  equal[i] = int(equal[i])
target = equal[0]
dfs(0,target);
print(ans);