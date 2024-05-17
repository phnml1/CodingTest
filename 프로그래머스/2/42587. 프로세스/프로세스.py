def solution(priorities, location):
    answer = []
    keys = []
    for k,v in enumerate(priorities):
        keys.append((k));
    while True:
        max_num = max(priorities);
        if max_num == -1:
            break;
        for i in range(len(priorities)):
            if max_num == priorities[i]:   
                answer.append(keys[i]);
                priorities[i] = -1;
                max_num = max(priorities)
                
    print(answer)                   
    return answer.index(location)+1