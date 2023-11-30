import sys
input = sys.stdin.readline

n = int(input());
arr = list(map(int,input().split()));
DP = [0 for _ in range(n)];
DP[0] = arr[0];
for i in range(1,n):
    DP[i] = max(DP[i-1]+arr[i],arr[i]);
print(max(DP));