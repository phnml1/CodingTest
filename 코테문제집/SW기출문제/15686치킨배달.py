from itertools import combinations


n,m = map(int,input().split());
arr = [];
houses = []
chicken = []
dir = [[0,1],[1,0],[-1,0],[0,-1]];
result = 1e9
for i in range(n):
  newarr = list(map(int,input().split()));
  for j in range(len(newarr)):
    if newarr[j] == 1:
      houses.append([i,j]);
    if newarr[j] == 2:
      chicken.append([i,j]);
  arr.append(newarr);
for case in combinations(chicken,m):
  res = 0;
  for house in houses:
    dis = 1e9;
    for a in case:
      x,y = house[0],house[1];
      temp = abs(x-a[0]) + abs(y-a[1]);
      dis = min(dis,temp)
    res += dis;
  result = min(result,res);
print(result)
