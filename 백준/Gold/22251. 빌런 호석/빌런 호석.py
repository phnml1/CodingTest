import sys;
input = sys.stdin.readline;

n,k,p,x = map(int, input().split());
result = 0;
numbers = [[0,1,2,4,5,6],[2,5],[0,2,3,4,6],[0,2,3,5,6],[1,2,3,5],[0,1,3,5,6],[0,1,3,4,5,6],[0,2,5],[0,1,2,3,4,5,6],[0,1,2,3,5,6]];
x = list(str(x));

if len(x) != k:
    for _ in range(k-len(x)):
        x.insert(0,'0');
        
def dfs(index,count,st):
    global result;
    if count>p:
        return;
    if index == k:
        if 0<count<=p and 0<int(st)<=n:
            result += 1;
        return;
    cur = set(numbers[int(x[index])]);
    for i in range(len(numbers)):
        compare = set(numbers[i]);
        cur_count = len(list(cur.difference(compare))) + len(list(compare.difference(cur)));
        if count + cur_count <=p:
            dfs(index+1,count + cur_count,st + str(i));
dfs(0,0,'');
print(result);