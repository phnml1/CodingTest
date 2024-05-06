import sys;
input = sys.stdin.readline;
n = int(input());
arr = [];
for _ in range(n):
  index,num = map(int,input().split());
  arr.append([index,num]);
arr.sort();

dp = [1] * (n);

for i in range(1,n):
  for j in range(i):
    if arr[i][1]>arr[j][1]:
      dp[i] = max(dp[j] + 1,dp[i]);
print(n - max(dp));