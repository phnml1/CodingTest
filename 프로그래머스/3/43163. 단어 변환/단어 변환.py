
def CanChange(s,t):
        diff = 0
        for s_ , t_ in zip(s,t):
            if s_ != t_:
                diff +=1
        if diff == 1:
            return True
        else: return False
def solution(begin, target, words):
    answer = [];
    visited = {}
    if target not in words:
        return 0;
    def dfs(cur,ch):
        nonlocal answer;
        if cur == target:
            answer.append(ch);
            return;
        if cur not in visited:
            visited[cur] = ch;
        else:
            if visited[cur] > ch:
                visited[cur] = ch;
        for i in words:
            count = 0;
            if CanChange(i,cur):
                if i in visited:
                    if visited[i]>=ch+1:
                        dfs(i,ch+1);
                if i not in visited:
                    dfs(i,ch+1);
                
    dfs(begin,0);
    if len(answer) !=0:
        return min(answer);
    return 0;