class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visited = [0] * numCourses  # 0: 미방문, 1: 방문중, 2: 완료

        def dfs(node):
            # 방문 중이면 사이클
            if visited[node] == 1:
                return False

            # 이미 완료된 노드는 다시 볼 필요 없음
            if visited[node] == 2:
                return True

            visited[node] = 1  # 방문 중

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 2  # 방문 완료
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
                