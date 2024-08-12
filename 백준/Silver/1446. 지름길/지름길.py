import sys;
from collections import defaultdict;
input = sys.stdin.readline;
n,d = map(int,input().split());
shortcuts = defaultdict(list);
dp = [];
for _ in range(n):
    s,e,dis = map(int,input().split());
    if e-s > dis:
        shortcuts[s].append((e,dis));
cur = 0;
for i in range(10001):
    dp.append(i);
while cur<=d:
    dp[cur] = min(dp[cur-1] + 1, dp[cur]); 
    if cur in shortcuts:
        for a in shortcuts[cur]:
            e,dis = a;
            dp[e] = min(dp[e],dp[cur] + dis);
    cur += 1;
print(dp[d]);
    