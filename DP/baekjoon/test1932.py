import sys
input = sys.stdin.readline;

n = int(input());
DP = [[0 for _ in range(n)] for _ in range(n)];
arr = [[0] for _ in range(n)];
for i in range(n):
  arr[i] = list(map(int,input().split()));
DP[0][0] = arr[0][0];
for i in range(1,n):
  for j in range(i+1):
    sum = 0;
    if j==0:
      sum = max(sum, DP[i-1][j]+arr[i][j])
    else:
      sum = max(sum, DP[i-1][j-1] + arr[i][j]);
    sum = max(sum, DP[i-1][j] + arr[i][j]) 
    DP[i][j] =sum;
print(max(DP[n-1]));