import sys
input = sys.stdin.readline
n = int(input());
bulbs = list(map(bool,map(int,input().rstrip())));
target = list(map(bool,map(int,input().rstrip())));
off = bulbs.copy();
on = bulbs.copy();
on[0] = not on[0];
on[1] = not on[1];
def change(st,count):
  st_copy = st[:]

  for i in range(1,n):
    if st_copy[i-1] == target[i-1]:
      continue
    count += 1;
    for j in range(i-1,i+2):
      if j<n:
        st_copy[j] = not st_copy[j];
  if st_copy == target:
    return count;
  else:
    return 1e9;
res = min(change(on,1),change(off,0));
if res != 1e9:
  print(res)
else:
  print(-1);