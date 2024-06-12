def solution(numbers, target):
    answer = 0
    def dfs(index, value):
        nonlocal answer;
        if index == len(numbers)-1:
            if value == target:
                answer+=1;
            return;
        dfs(index+1, value + numbers[index+1]);
        dfs(index+1, value - numbers[index+1]);
        
    dfs(-1,0);
    return answer