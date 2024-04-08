s = int(input());
sum,count = 0,0;
i=1;
while True:
  if sum==s:
    break;
  elif sum > s:
    count -= 1;
    break;
  sum+=i
  count += 1;
  i+=1;
  
print(count);