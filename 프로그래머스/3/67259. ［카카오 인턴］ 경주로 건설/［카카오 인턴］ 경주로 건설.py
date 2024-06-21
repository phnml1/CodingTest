import heapq
def solution(board):
    max_x,max_y = len(board)-1,len(board[0])-1
    dir = [[(0,1),(0,-1)],[(1,0),(-1,0)]]
    queue = [(0,0,0,0),(0,0,0,1)];
    heapq.heapify(queue);
    costs = [[[1e9 for _ in range(2)] for _ in range(len(board[0]))] for _ in range(len(board))]
    while queue:
        cost,x,y,d = heapq.heappop(queue);
        for i in range(2):
            for j in range(2):
                dx,dy = dir[i][j];
                next_x,next_y = x + dx, y + dy;
                if 0<=next_x<=max_x and 0<=next_y<=max_y:
                    if board[next_x][next_y] != 1:
                        if i != d:
                            next_cost = cost + 600;        
                        if i == d:
                            next_cost = cost + 100;
                        if costs[next_x][next_y][i] > next_cost:
                            costs[next_x][next_y][i] = next_cost;
                            heapq.heappush(queue,(next_cost,next_x,next_y,i));
    return min(costs[max_x][max_y])