class Solution(object):
    def allPathsSourceTarget(self, graph):
        visited = [False] * len(graph)
        paths = []
        new_path = [0]

        def dfs(i, path):
            if i == len(graph) - 1:
                tmp = [i for i in path]
                paths.append(tmp)
                return
            visited[i] = True
            for neighbor in graph[i]:
                if not visited[neighbor]:
                    path.append(neighbor)
                    dfs(neighbor, path)
                path.pop()
                visited[i] = False

        dfs(0, new_path)
        return paths


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))

