d = [0]*30001;
n = int(input());
cur = 2;
d[1] = 3;
d[0] = 1;
while cur<=n-1:
  d[cur] = d[cur-1] + (d[cur-2] * 2);
  cur+=1;
print(d[n-1]);