class Solution(object):
    # def findJudge(self, n: int, trust: list[list[int]]):
    #     adjacency_matrix = [[0] * n for i in range(n)]
    #     for edge in trust:
    #         s = edge[0]
    #         d = edge[1]
    #         adjacency_matrix[s-1][d-1] = 1
    #
    #     for source in range(len(adjacency_matrix)):  # index
    #         if sum(adjacency_matrix[source]) == 0:
    #             edge_sum = 0
    #             dest = source
    #             for src in adjacency_matrix:
    #                 edge_sum += src[dest]
    #             if edge_sum == n - 1:
    #                 return dest + 1
    #     return -1

    def findJudge(self, n: int, trust: list[list[int]]):
        incoming = {key: [] for key in range(1, n+1)}
        outgoing = {key: [] for key in range(1, n+1)}
        for edge in trust:
            source = edge[0]
            dest = edge[1]
            if dest not in outgoing[source]:
                outgoing[source].append(dest)
            if source not in incoming[dest]:
                incoming[dest].append(source)
        for key in incoming:
            if len(incoming[key]) == n-1 and len(outgoing[key]) == 0:
                return key
        return -1






if __name__ == '__main__':
    sol = Solution()
    t = [[1, 2], [3, 2], [4, 2], [5, 2], [3, 4]]
    print(sol.findJudge(5, t))

