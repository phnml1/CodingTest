from collections import defaultdict
import sys;

input = sys.stdin.readline;
t = int(input());
for _ in range(t):
  st = input();
  k = int(input());
  index = 0;
  alphabets = defaultdict(list);
  max_result,min_result = 0,1e9;
  
  while index < len(st):
    alphabets[st[index]].append(index);
    if len(alphabets[st[index]]) == k:
      length = alphabets[st[index]][-1] - alphabets[st[index]][0] + 1;
      max_result = max(max_result,length);
      min_result = min(min_result,length);
      alphabets[st[index]].pop(0);
    index+=1;
  if max_result == 0 or min_result == 1e9:
    print(-1);
  else:
    print(min_result,max_result);