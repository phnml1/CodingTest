import sys;
input = sys.stdin.readline;

n = int(input());
arr = [];
result = 0;
max_arr = [0,0];
for i in range(n):
    cur = list(map(int,input().split()));
    if cur[1] > max_arr[1]:
        max_arr = cur;
    arr.append(cur);
    
arr.sort();
stack = [];
index = arr.index(max_arr);
result = max_arr[1];
height = arr[0][1];
for i in range(index):
    if height<arr[i+1][1]:
        result += height * (arr[i+1][0] - arr[i][0]);
        height = arr[i+1][1];
    else:
        result += height * (arr[i+1][0] - arr[i][0]);
        
        
height = arr[-1][1];
for i in range(n-1,index,-1):
    if height < arr[i-1][1]:
        result += height * (arr[i][0] - arr[i-1][0]);
        height = arr[i-1][1];
    else:
        result += height * (arr[i][0] - arr[i-1][0]);
        
print(result);