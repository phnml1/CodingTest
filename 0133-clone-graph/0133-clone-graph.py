"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def __init__(self):
        # 이미 복사한 노드들을 저장하는 딕셔너리 (무한 루프 방지용)
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # 1. 이미 방문(복사)한 노드라면 그 복사본을 즉시 반환
        if node in self.visited:
            return self.visited[node]

        # 2. 현재 노드의 복사본 생성 (이웃은 아직 비어있음)
        clone_node = Node(node.val)
        self.visited[node] = clone_node

        # 3. 원본 노드의 이웃들을 순회하며 복사본의 이웃 채우기
        for neighbor in node.neighbors:
            # 재귀적으로 이웃들을 복사해서 현재 노드의 neighbors에 추가
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node
