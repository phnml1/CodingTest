import sys
input = sys.stdin.readline;
n = int(input());
arr = []
for _ in range(n):
  arr.append(int(input()));
dp = [0 for _ in range(n)];
dp[0] = 1;
for i in range(1,n):
  for j in range(i):
    if arr[j]<arr[i]:
      dp[i] = max(dp[j]+1,dp[i]);
print(int(n-max(dp)));
  
  