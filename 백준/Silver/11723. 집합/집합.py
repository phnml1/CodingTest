import sys;

input = sys.stdin.readline;
n = int(input());
s = set();
for _ in range(n):
  arr = list(input().split());
  if len(arr) == 2:
    calc, num = arr[0],arr[1];
    if calc == 'add':
      s.add(int(num));
    elif calc == 'remove':
      if int(num) in s:
        s.remove(int(num));
    elif calc == 'toggle':
      if int(num) in s:
        s.remove(int(num));
      else:
        s.add(int(num));
    else:
      if int(num) in s: print(1);
      else: print(0);
  else:
    if arr[0] == 'all':
      s = set([i for i in range(1,21)]);
    else:
      s = set([]);
      