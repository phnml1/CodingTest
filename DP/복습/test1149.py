from itertools import permutations;
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int,input().split())));
result = 1e9;
DP = [[0 for _ in range(3)] for _ in range(n)];
for i in range(3):
  DP[0][i] = arr[0][i];
for i in range(1,n):
  for j in range(3):
    if j==0:
      DP[i][j] = arr[i][j] + min(DP[i-1][j+1],DP[i-1][j+2]);
    elif j==1:
      DP[i][j] = arr[i][j] + min(DP[i-1][j-1],DP[i-1][j+1]);
    else:
      DP[i][j] = arr[i][j] + min(DP[i-1][j-1],DP[i-1][j-2]);
print(min(DP[n-1]))