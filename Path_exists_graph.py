class Solution(object):
    def __init__(self):
        self.res = False
        self.visited = []
        self.neighbors = {}

    def dfs(self, source, destination):
        self.visited[source] = True
        if source == destination:
            self.res = True
        else:
            for neighbor in self.neighbors[source]:
                if not self.visited[neighbor]:
                    self.dfs(neighbor, destination)

    def validPath(self, n, edges, source, destination):
        self.visited = [False] * n
        self.neighbors = {key: [] for key in range(n)}

        for s, d in edges:
            self.neighbors[s].append(d)
            self.neighbors[d].append(s)

        self.dfs(source, destination)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    print(sol.validPath(5, [[0, 1], [0, 3], [1, 3], [2, 3]], 0, 4))

