import sys
input = sys.stdin.readline
n, k = map(int, input().split());
stuff = [(0,0)];
DP = [[0] * (k+1) for _ in range(n+1)];

for _ in range(n):
  stuff.append(list(map(int,input().split())));

for i in range(1,n+1):
  w,v = stuff[i];
  for j in range(1,k+1):
    if j-w <= 0:
      DP[i][j] = DP[i-1][j];
    else:
      DP[i][j] = max(DP[i-1][j],DP[i-1][j-w]+v);
print(DP)
print(DP[n][k]);
