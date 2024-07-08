class Solution(object):
    def makeConnected(self, n, connections):
        parent = [i for i in range(n)]
        rank = [1] * n
        operations = 0
        connected = 1

        def find(i):
            if parent[i] != i:
                return find(parent[i])
            return i

        def connect(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            rank_a = rank[root_a]
            rank_b = rank[root_b]

            if rank_a >= rank_b:
                parent[root_b] = root_a
                rank[root_a] += 1
            else:
                parent[root_a] = root_b
                rank[root_b] += 1
            return True

        for source, dest in connections:
            if not connect(source, dest):
                operations += 1
            else:
                connected += 1

        if operations >= n-connected:
            return n-connected
        return -1


if __name__ == '__main__':
    sol = Solution()
    c = [[1, 5], [1, 7], [1, 2], [1, 4], [3, 7], [4, 7], [3, 5], [0, 6], [0, 1], [0, 4], [2, 6], [0, 3], [0, 2]]
    print(sol.makeConnected(12, c))
