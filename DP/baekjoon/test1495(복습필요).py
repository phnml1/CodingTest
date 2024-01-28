n,s,m = map(int,input().split());
arr = list(map(int,input().split()));
#시간 초과
# DP = [0 for _ in range(n+1)];
# result = [];
# DP[0] = s;
# def volume_modify(plus,DP,i):
#   if plus == True:
#       DP[i] = DP[i-1]+ arr[i-1]
#   else:
#       DP[i] = DP[i-1] - arr[i-1]
#   if i>=n:
#     result.append(DP[i]);
#   else:
#     copydp = copy.deepcopy(DP);
#     if 0<=DP[i] + arr[i]<=m:
#       volume_modify(True,copydp,i+1);
#     if 0<= DP[i] - arr[i] <=m:
#       volume_modify(False,copydp,i+1);
# if 0<=DP[0] + arr[0]<=m:
#   volume_modify(True,DP,1);
# if 0<=DP[0] - arr[0] <=m:
#   volume_modify(False,DP,1);
# if len(result)>=1:
#   print(max(result));
# else:
#   print(-1);
d = [[0] * (m+1) for _ in range(n+1)];
d[0][s] = 1;
for i in range(1,n+1):
  for j in range(m+1):
    if d[i-1][j] != 0:
      if j + arr[i-1] <=m:
        d[i][j+arr[i-1]] = 1;
      if j - arr[i-1] >= 0:
        d[i][j-arr[i-1]] = 1;
result = -1
for i in range(m+1):
  if d[n][i] == 1:
    result = i;
print(result);