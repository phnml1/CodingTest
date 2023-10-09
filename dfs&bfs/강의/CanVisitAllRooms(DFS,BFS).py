from collections import deque

#DFS
def canVisitAllRooms(rooms): 
    visited = [False] * len(rooms);
    #혹은 딕셔너리나 해쉬set도가능
    # v에 연결되어 있는 모든 vertax에 방문할거다.
    def dfs(v):
        visited.append(v)
        for next_v in rooms[v]:
            # 리스트에 사용하면 O(n)
            # if next_v not in visited:
            if visited[next_v] ==False:
                dfs(next_v);
        dfs(0);
    return all(visited);

#BFS
def canVisitAllRoomsBFS(rooms): 
    visited = [False] * len(rooms);
    #혹은 딕셔너리나 해쉬set도가능
    # v에 연결되어 있는 모든 vertax에 방문할거다.
    def bfs(v):
        queue = deque();
        queue.append(v);
        visited[v] = True;
        while queue:
            cur_v = queue.popleft();
            for next_v in rooms[cur_v]:
                if visited[next_v] ==False:
                    queue.append(next_v);
                    visited[next_v]=True;
        
    bfs(0)
    
    return all(visited);
rooms = [[1,3],[2,4],[0],[4],[],[3,4]];
print(canVisitAllRoomsBFS(rooms))