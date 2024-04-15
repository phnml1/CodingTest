import sys; 
input = sys.stdin.readline;

t = int(input());
arr = []
for _ in range(t):
  arr.append(int(input()));

DP = [0 for _ in range(10001)];
DP[0] = 1;
for i in range(1,4):
  for j in range(i,10001):
    DP[j] = DP[j-i]+DP[j];
for num in arr:
  print(DP[num])