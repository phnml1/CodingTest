n,l = map(int,input().split());
arr = []
result = 0;
for _ in range(n):
  arr.append(list(map(int,input().split())));
def check(line):
  visited = [False for _ in range(n)]
  global l;
  for i in range(n-1):
    if line[i] == line[i+1]:
      continue;
    elif line[i] < line[i+1]:
      if line[i+1] - line[i] == 1:
        temp = line[i];
        for j in range(i,i-l,-1):
          if 0<=j<n:
            if temp != line[j]:
              return False;
            elif visited[j]:
              return False
            visited[j] = True;
          else:
            return False;    
      else:
        return False;
    elif line[i] > line[i+1]:
      if line[i] - line[i+1] == 1:
        temp = line[i+1];
        
        for j in range(i+1,i+l+1):
          if 0<=j<n:
            if line[j] != temp:
              return False;
            elif visited[j]:
              return False
            visited[j] = True;
          else:
            return False;
      else:
        return False;
  return True;

for line in arr:
  if check(line):
    result += 1;
for i in range(n):
  temp = []
  for j in range(n):
    temp.append(arr[j][i]);
  if check(temp):
    result += 1;
print(result);