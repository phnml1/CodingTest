from collections import deque


n = int(input());
arr= deque([i for i in range(1,n+1)]);
i=1;
while len(arr) > 1:
  node = arr.popleft();
  if i%2 == 0:
    arr.append(node);
  i+=1;
print(arr[0]);
    