import copy
n,m = map(int,input().split());
def dfs(arr,index):
    if index == m:
        print(' '.join(arr));
        return;
    for i in range(1,n+1):
        new_arr = copy.deepcopy(arr);
        if str(i) not in new_arr:
            new_arr.append(str(i));
            dfs(new_arr,index+1);
dfs([],0);