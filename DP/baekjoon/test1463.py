n = int(input());
d = [10000001]*(n+1);
d[n] = 0;
for i in range(n,0,-1):
  if i % 2 ==0:
    d[i//2] = min(d[i//2],d[i]+1);
  if i % 3 ==0:
    d[i//3] = min(d[i//3],d[i]+1);
  d[i -1] = min(d[i-1],d[i]+1);
print(d[1]); 