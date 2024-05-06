import sys
input = sys.stdin.readline;
n = int(input());
arr = list(map(int,input().split()));
dp = [1] * n;
reverse_dp = [1]*n;
result = 0;
for i in range(n):
  for j in range(i):
    if arr[i]>arr[j]:
      dp[i] = max(dp[j]+1,dp[i]);

for i in range(n-1,-1,-1):
  for j in range(n-1,i-1,-1):
    if arr[i]>arr[j]:
      reverse_dp[i] = max(reverse_dp[j]+1,reverse_dp[i]);
for i in range(n):
  result = max(result,dp[i] + reverse_dp[i]-1)    
print(result);