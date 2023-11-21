n = int(input());
arr1 = list(map(int,input().split()));
m = int(input());
arr2 = list(map(int,input().split()));
aa = {}
for i in range(n):
  if arr1[i] in aa:
    aa[arr1[i]] += 1;
  else:
    aa[arr1[i]] = 1;
for i in range(m):
  if arr2[i] in aa:
    print(aa[arr2[i]], end= ' ')
  else:
    print(0,end = ' ');