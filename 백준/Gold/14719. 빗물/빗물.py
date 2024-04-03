h,w = map(int,input().split());
blocks = list(map(int,input().split()));
stack = []
left_max, right_max = 0,0;
result = 0;
for i in range(1,len(blocks)-1):
  left_max = max(blocks[:i]);
  right_max = max(blocks[i:]);
  compare = min(left_max,right_max);
  if compare > blocks[i]:
    result += (compare - blocks[i])
print(result);