import sys
input = sys.stdin.readline;
n = int(input())
arr = list(map(int,input().split()));
dp = [[0 for _ in range(n+1)] for _ in range(n+1)];
for i in range(n):
  for j in range(n-i):
    start = j;
    end = j+i;
    if start == end:
      dp[start][end] = 1;
    elif arr[start] == arr[end]:
      if end-start == 1:
          dp[start][end] = 1;
      else:
        if dp[start+1][end-1] == 1:
          dp[start][end] = 1;
t = int(input())
for _ in range(t):
  n,m = map(int,input().split());
  print(dp[n-1][m-1]);       