# class Solution(object):
#
#     def eventualSafeNodes(self, graph):
#         visited = [False] * len(graph)
#         safe = {node: True for node in range(len(graph))}
#
#         def dfs(v):
#             if visited[v]:
#                 for node in range(len(visited)):
#                     if visited[node]:
#                         safe[node] = False
#                 return
#             visited[v] = True
#             for neighbor in graph[v]:
#                 dfs(neighbor)
#             visited[v] = False
#
#         for i in range(len(graph)):
#             if safe[i]:
#                 dfs(i)
#         res = []
#         for node in safe:
#             if safe[node]:
#                 res.append(node)
#         return res


class Solution(object):

    def eventualSafeNodes(self, graph):
        safe = {}

        def dfs(v):
            if v in safe:
                return safe[v]
            safe[v] = False
            for neighbor in graph[v]:
                if not dfs(neighbor):
                    return safe[v]

            safe[v] = True
            return safe[v]

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res


if __name__ == '__main__':
    sol = Solution()
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(sol.eventualSafeNodes(graph))
