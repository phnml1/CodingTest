n,k = map(int,input().split());
datas = [[0]*(k+1)]
for i in range(n):
  datas.append(list(map(int,input().split())));
DP = [[0 for _ in range(k+1)] for _ in range(n+1)];
for i in range(1,n+1):
  w,v = datas[i];
  for j in range(1,k+1):
    if j-w<0:
      DP[i][j] = DP[i-1][j];
    else:
      DP[i][j] = max(DP[i-1][j-w] + v, DP[i-1][j]);
print(DP[n][k]);