from collections import defaultdict
import sys;

input = sys.stdin.readline;
n,k = map(int,input().split());
countrys = defaultdict(list);
result_key = ();
result = 0;
for _ in range(n):
  n,g,s,b = map(int,input().split());
  if n == k:
    result_key = (g,s,b);
  countrys[(g,s,b)].append(n);
keys = sorted(list(countrys.keys()),reverse = True);
for i in keys[:keys.index(result_key)]:
  result += len(countrys[i]);
print(result+1);
