n,s = map(int,input().split());
arr = list(map(int,input().split()));
result = 1e9;
prev,cur = 0,0;
sum = 0;
while 1:
  if sum>=s:
    length = cur - prev;
    result = min(length,result);
    sum -= arr[prev];
    prev += 1;
  elif cur == n:
    break;
  else:
    sum += arr[cur];
    cur += 1;
    
if result == 1e9:
  print(0);
else:
  print(result);