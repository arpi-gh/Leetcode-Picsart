class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        incoming = {node: [] for node in range(n)}
        for source, destination in edges:
            incoming[destination].append(source)

        visited = [False] * n
        res = []
        for node in incoming:
            if not incoming[node]:
                res.append(node)

        return res