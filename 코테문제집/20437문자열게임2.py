# #시간초과
# import sys
# input = sys.stdin.readline;
# t = int(input())
# results = []

# # def slide_window(w,k):
# #   global min_num,max_num;
# #   wcases = set(w);
# #   for i in range(k,len(w)):
# #     window = w[:i];
# #     for case in list(wcases):
# #       if window.count(case) == k:
# #         min_num =  min(min_num,len(window));
# #         if window[0]==case and window[0]== window[-1]:
# #           max_num = max(max_num,len(window));

# #     for j in range(i,len(w)):
# #       window += w[j];
# #       window = window[1:];
# #       for case in list(wcases):
# #         if window.count(case) == k:
# #           min_num =  min(min_num,len(window));
# #           if window[0]==case and window[0]== window[-1]:
# #             max_num = max(max_num,len(window));
# #   return -1;
# # for _ in range(t):
# #   min_num = 1e9;
# #   max_num = -1;
# #   w = input().rstrip();
# #   k = int(input());
# #   slide_window(w,k);
# #   if min_num != -1 and max_num != -1:
# #     results.append((min_num,max_num));
# #   else:
# #     results.append([-1]);
# # for result in results:
# #   if len(result) == 1:
# #     print(-1)
# #   else:
# #     min_num,max_num = result;
# #     print(min_num,max_num);

import sys
from collections import defaultdict
t = int(input())
for _ in range(t):
  w = sys.stdin.readline().rstrip()
  k = int(input())
  
  char_dict = defaultdict(list);
  for idx, char in enumerate(w):
    if w.count(char) >= k:
      char_dict[char].append(idx)
  short = 1e9
  long = 0
  for char, idx_list in char_dict.items():
    if len(idx_list) == k:
      length = idx_list[-1] - idx_list[0] + 1
      if length <short:
        short = length
      if length > long:
        long = length
    elif len(idx_list) > k:
      st = 0
      while 1:
        nd = st + (k-1)
        length = idx_list[nd] - idx_list[st] + 1
        
        if length < short:
          short = length
        if length > long:
          long = length
        
        if nd == (len(idx_list)-1):
          break;
        st += 1;
  if long==0 and short>10000:
    print(-1)
  else:
    print(short,long);