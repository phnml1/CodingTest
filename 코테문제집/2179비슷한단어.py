import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append([i,input().rstrip()]);
sorted_arr = sorted(arr, key = lambda x: x[1]);
prev = sorted_arr[0][1]
max_count = 0;
result = 0;
min_index = 1e9; 
for i in range(1,n):
  cur = sorted_arr[i][1];
  min_len = min(len(prev),len(cur));
  count = 0;
  if prev == cur:
    prev=cur;
    continue;
  for j in range(min_len):
    if prev[j] == cur[j]:
      count += 1;
    else:
      break;
  if max_count <count:
    max_count = count;
    result = (sorted_arr[i-1][0],sorted_arr[i][0]);
  if max_count==count:
    index = min(sorted_arr[i-1][0],sorted_arr[i][0]);
    if index<min_index:
      result = (sorted_arr[i-1][0],sorted_arr[i][0]);
      min_index = index
  prev = cur;
prev,cur = result;
if prev<cur:
  print(arr[prev][1]);
  print(arr[cur][1]);
else:
  print(arr[cur][1]);
  print(arr[prev][1]);
