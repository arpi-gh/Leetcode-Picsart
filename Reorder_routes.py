class Solution(object):
    def __init__(self):
        self.reverse = 0

    def minReorder(self, n, connections):
        edges = {node: [] for node in range(n)}
        neighbors = {node: [] for node in range(n)}
        q = []
        visited = [False] * n
        for s, d in connections:
            edges[s].append(d)
            neighbors[s].append(d)
            neighbors[d].append(s)

        q.append(0)
        while q:
            current = q.pop(0)
            visited[current] = True
            for neigh in neighbors[current]:
                if not visited[neigh]:
                    q.append(neigh)
                    if current not in edges[neigh]:
                        self.reverse += 1
        return self.reverse


if __name__ == '__main__':
    sol = Solution()
    c = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(sol.minReorder(6, c))
