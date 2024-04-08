from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline;

n = int(input());
max_length = 1000000;
arr = [9,8,7,6,5,4,3,2,1,0];
i = 1;
cases = []
for i in range(1,11):
  for j in combinations(range(10),i):
    num = sorted(list(j), reverse=True);
    cases.append(int(''.join(str(e) for e in num)));
cases.sort();
print(cases[n] if n<=len(cases) else -1);
  
