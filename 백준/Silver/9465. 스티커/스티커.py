t = int(input());

for _ in range(t):
  n = int(input());
  arr = [list(map(int,input().split())),list(map(int,input().split()))];
  DP = [[0 for _ in range(n)] for _ in range(2)];
  DP[0][0] = arr[0][0];
  DP[1][0] = arr[1][0];
  result = 0;
  if n>=2: 
    DP[0][1] = DP[1][0] + arr[0][1];
    DP[1][1] = DP[0][0] + arr[1][1];
  if n>=3:
    for i in range(2,n):
      DP[0][i] = arr[0][i] + max(DP[1][i-1],DP[1][i-2]);
      DP[1][i] = arr[1][i] + max(DP[0][i-1],DP[0][i-2]);
  for a in DP:
    result = max(result,max(a));
  print(result);