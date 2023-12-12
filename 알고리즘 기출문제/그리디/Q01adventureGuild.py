# 내 풀이
# n = int(input());
# arr = list(map(int, input().split()));
# arr.sort(reverse=True);
# count = 0;
# index = 0;
# while index<len(arr):
#   num = arr[index];
#   index = index+num;
#   count += 1;
# print(count);
# 책 풀이
n = int(input());
arr = list(map(int, input().split()));
arr.sort()
result = 0;
count = 0;

for i in arr:
  count += 1;
  if count>=i:
    result += 1
    count = 0
print(result);