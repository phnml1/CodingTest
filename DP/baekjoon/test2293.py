import sys
input = sys.stdin.readline;
n,k = map(int,input().split());
arr = []
for i in range(n):
  arr.append(int(input()));
arr.sort();
DP = [0 for _ in range(k+1)];
DP[0] = 1;
for i in arr:
  for j in range(i,k+1):
    if j-i>=0:
      DP[j]+=DP[j-i];
print(DP[k]);