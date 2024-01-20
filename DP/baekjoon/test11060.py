from sys import stdin
input = stdin.readline
n = int(input());
arr = list(map(int,input().split()));
index = 0;
jump = 0
# dp = [n+1] * n;
# dp [0] = 0
# for i in range(n):
#   for j in range(1,arr[i]+1):
#     if i+j >=n:
#       break;
#     dp[i+j] = min(dp[i+j],dp[i]+1);
# print(dp[n-1] if dp[n-1] != n+1 else -1);
while index<n-1:
  data = arr[index];
  if data == 0:
    jump = -1;
    break;
  next = [0,0];
  for i in range(1,data+1):
    if index + i<=n-1:
      next[0] = max(next[0], index+i + arr[index + i])
      if next[0] == index+i + arr[index + i]:
        next[1] = index+i;
    else:
      next[1] = n;
      break;
  index = next[1];
  jump += 1;
print(jump);