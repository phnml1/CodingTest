# p397
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x]);
  return parent[x];

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a;
  else:
    parent[a] = b;
g = int(input());
p = int(input());
parent = [0] * (g+1)
for i in range(1,g+1):
  parent[i] = i
result = 0;
for _ in range(p):
  data = find_parent(parent,int(input()))
  if data == 0:
    break
  union_parent(parent,data,data-1)
  result += 1
print(result);
# 내 풀이
# for i in range(p):
#   j = int(input());
#   isdocked = False;
#   for a in range(j,0,-1):
#     if docked[a] == False:
#       docked[a] = True;
#       isdocked = True;
#       break;
#   if isdocked == False:
#     break;
#   else:
#     result += 1;
# print(result);
    
