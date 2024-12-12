n,m = map(int,input().split());
def dfs(arr):
   if len(arr) == m:
        print(*arr);
        return
   for i in range(1,n+1):
        if i not in arr:
            arr.append(i);
            dfs(arr);
            arr.pop();
dfs([]);