from sys import stdin
input = stdin.readline
n,k = map(int,input().split());
arr = []
for i in range(n):
  arr.append(int(input()));
# 메모리초과
# DP = [[1 for _ in range(k+1)] for _ in range(n)];
# for i in range(1,k+1):
#   DP[0][i] = 1;
# for i in range(1,n):
#   for j in range(1,k+1):
#     if j - arr[i] >= 0:
#       DP[i][j] = DP[i-1][j] + DP[i][j-arr[i]];
#     else:
#       DP[i][j] = DP[i-1][j];
# print(DP[n-1][k]);
DP = [0 for _ in range(k+1)];
DP[0] = 1;
for data in arr:
  for j in range(1,k+1):
    if j - data >= 0:
      DP[j] += DP[j-data]; 
print(DP[k]);