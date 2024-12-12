from itertools import combinations
n,s = map(int,input().split());
arr = list(map(int,input().split()));
result = 0;
for i in range(1, len(arr)+1):
    for cur in list(combinations(arr,i)):
        if sum(cur) == s:
            result += 1;
print(result);