import sys;
input = sys.stdin.readline;
def dfs(idx,cnt):
    global result;   
    if cnt == k-5:
        tmp = 0;
        for word in words:
            flag = True;
            for w in word:
                if check[ord(w)-ord('a')] == 0:
                    flag = False;
                    break;
            if flag:
                tmp += 1;
        result = max(result, tmp);
        return;
    
    for i in range(idx,26):
        if check[i] == 0:
            check[i] = 1;
            dfs(i,cnt+1);
            check[i] = 0;

n,k = map(int,input().split());
words = [];
result = 0;
check = [0] * 26;
if k<5:
    print(0);
    exit();
if k == 26:
    print(n);
    exit();
    
for _ in range(n):
    words.append(set(input().rstrip()));
    
for w in ['a','n','t','i','c']:
    check[ord(w) - ord('a')] = 1;

dfs(0,0);
print(result);