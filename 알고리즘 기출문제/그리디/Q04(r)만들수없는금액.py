n = int(input());
arr = list(map(int,input().split()));
arr.sort();
result = 1;
for x in arr:
  if result < x:
    break
  result += x;
  
print(result)
      