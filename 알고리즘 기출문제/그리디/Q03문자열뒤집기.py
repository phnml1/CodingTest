a = input();
arr = [0,0];
index = 1;
prev = int(a[0]);
while index<len(a):
  if a[prev] != a[index]:
    arr[prev] += 1;
  prev = int(a[index]);
  index += 1;
print(min(arr));