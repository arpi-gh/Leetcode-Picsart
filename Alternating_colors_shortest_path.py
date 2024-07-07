class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        edges = {node: [] for node in range(n)}
        res = [-1] * n
        for source, destination in redEdges:
            edges[source].append((destination, 'red'))
        for source, destination in blueEdges:
            edges[source].append((destination, 'blue'))

        visited = set()

        queue = [(0, '', 0)]
        # destination, color, distance  (1, 'blue', 1),  (3, 'red', 2), (4, 'red', 2)
        while queue:
            node, color, distance = queue.pop(0)
            if (node, color) not in visited:
                for neighbor, edge_color in edges[node]:
                    if edge_color != color:
                        queue.append((neighbor, edge_color, distance+1))
                visited.add((node, color))
                if res[node] == -1:
                    res[node] = distance

        return res


if __name__ == '__main__':
    red = [[0, 1], [0, 2]]
    blue = [[1, 0]]
    sol = Solution()
    print(sol.shortestAlternatingPaths(5, red, blue))
