n,s = map(int,input().split());
arr = list(map(int,input().split()));
result = 0;
def dfs(cur, index):
    global result;
    if sum(cur) == s and len(cur) >0:
        result += 1;
    for i in range(index, len(arr)):
        cur.append(arr[i]);
        dfs(cur,i+1);
        cur.pop();
dfs([],0);
print(result);