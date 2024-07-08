class Solution(object):
    def minReorder(self, n, connections):
        edges = {node: [] for node in range(n)}
        neighbors = {node: [] for node in range(n)}
        visited = [False] * n
        reverse = 0
        order = []
        q = []
        for s, d in connections:
            edges[s].append(d)
            neighbors[s].append(d)
            neighbors[d].append(s)

        q.append(0)
        while q:
            current = q.pop(0)
            order.append(current)
            for n in neighbors[current]:
                if n not in order:
                    q.append(n)

        def dfs(src):
            nonlocal reverse
            visited[src] = True
            for neighbor in edges[src]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    reverse += 1

        for node in order:
            if not visited[node]:
                dfs(node)

        return reverse


if __name__ == '__main__':
    sol = Solution()
    c = [[1,2],[2,0]]
    print(sol.minReorder(3, c))
