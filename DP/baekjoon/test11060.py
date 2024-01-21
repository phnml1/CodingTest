from sys import stdin
input = stdin.readline
n = int(input());
arr = list(map(int,input().split()));
dp = [n+1]*n
dp[0] = 0;
for i in range(n):
  for j in range(arr[i] + 1):
    if i+j < n:
      dp[i+j] = min(dp[i]+1,dp[i+j]);
print(dp[n-1] if dp[n-1]!=n+1 else -1);
    