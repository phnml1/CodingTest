import sys
input = sys.stdin.readline
n = int(input());
arr = [];
for i in range(n):
  arr.append(int(input()));
DP = [(0,0) for _ in range(n)];
DP[0] = (arr[0],arr[0]);
if n>=2:
  DP[1] = (arr[0]+arr[1],arr[1]);
if n>=3:
  for i in range(2,n):
    for j in range(1,3):
      dp1,dp2 = DP[i-j];
      cur1,cur2 = DP[i];
      if j == 1:
        cur1 = dp2+arr[i];
        DP[i] = (cur1,cur2);
      if j==2:
        cur2 = max(dp1+arr[i],dp2+arr[i])
        DP[i] = (cur1,cur2);
print(max(DP[n-1]));