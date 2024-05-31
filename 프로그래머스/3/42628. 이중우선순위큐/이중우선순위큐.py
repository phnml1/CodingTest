import heapq

def solution(operations):
    queue = []
    for oper in operations:
        arr = oper.split(' ');
        if arr[0] == 'I':
            heapq.heappush(queue,int(arr[1]));
        elif arr[0] == 'D':
            if queue:
                if arr[1] == '-1':
                    heapq.heappop(queue);
                elif arr[1] == '1':
                    queue.pop();
    queue.sort()
    if len(queue)==0:
        return [0,0];
    else:
        return [queue[-1],queue[0]]