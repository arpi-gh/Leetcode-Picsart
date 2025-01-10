

class Solution(object):
    def getAncestors(self, n, edges):
        outgoing = [[] for node in range(n)]
        incoming = [[] for node in range(n)]
        res = [set() for node in range(n)]
        for source, destination in edges:
            outgoing[source].append(destination)
            incoming[destination].append(source)

        q = []
        for i in range(len(incoming)):
            if not incoming[i]:
                q.append(i)

        while q:
            current = q.pop(0)
            for neighbor in outgoing[current]:
                q.append(neighbor)
                res[neighbor].update(res[current])
                res[neighbor].add(current)

        return [sorted(list(elem)) for elem in res]


if __name__ == '__main__':
    sol = Solution()
    g = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    print(sol.getAncestors(8, g))
