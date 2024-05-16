import math
def solution(progresses, speeds):
    queue = [];
    answer = []
    queue.append(math.ceil((100 - progresses[0])/speeds[0]));
    for i in range(1,len(progresses)):
        remain = math.ceil((100 - progresses[i])/speeds[i]);
        if queue[0] < remain:
            answer.append(len(queue));
            queue = [];
        queue.append(remain);
    if len(queue)>0:
        answer.append(len(queue));
    return answer