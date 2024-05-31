def solution(numbers, target):
    answer = 0
    def dfs(cur,index, calc):
        nonlocal answer;
        if index == len(numbers)-1:
            if cur == target:
                answer+=1;
            return;
        if calc == 0:
            cur += numbers[index+1];
        else:
            cur -= numbers[index+1];
        dfs(cur,index+1,0);
        dfs(cur,index+1,1);
        
    dfs(numbers[0],0,0);
    dfs(numbers[0],0,1);
    dfs(-numbers[0],0,0);
    dfs(-numbers[0],0,1);
    return answer//2