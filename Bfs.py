
from collections import deque

#닥치고 외우기
def bfs (root):
    #방문한노드 추가용
    visited = []
    if root is None:
        return 0
    #FIFO 큐사용
    q = deque()
    q.append(root)
    
    while q:
        #q이므로
        cur_node = q.popleft()
        #방문한순서 리턴하기위해 append
        visited.append(cur_node.value)
        
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

bfs(root)