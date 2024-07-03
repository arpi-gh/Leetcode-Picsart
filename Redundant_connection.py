class Solution(object):
    def findRedundantConnection(self, edges):
        parent = {i: i for i in range(1, len(edges) + 1)}
        rank = {i: 1 for i in range(1, len(edges) + 1)}

        def find(i):
            if parent[i] != i:
                return find(parent[i])
            return parent[i]

        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x == parent_y:
                return False
            rank_x = rank[parent_x]
            rank_y = rank[parent_y]

            if rank_x >= rank_y:
                rank[parent_x] += 1
                parent[parent_y] = parent_x
            else:
                rank[parent_y] += 1
                parent[parent_x] = parent_y

            return True

        for source, dest in edges:
            if not union(source, dest):
                return [source, dest]


# class Solution(object):
#     def findRedundantConnection(self, edges):
#         conns = {}
#         for source, dest in edges:
#             if source not in conns:
#                 conns[source] = []
#             if dest not in conns:
#                 conns[dest] = []
#             conns[source].append(dest)
#             conns[dest].append(source)
#
#         def bfs(v, q):
#             in_the_tree = {node: False for node in conns}
#             while q:
#                 node = q.pop(0)
#                 in_the_tree[node] = True
#                 for child in conns[node]:
#                     if not in_the_tree[child]:
#                         if child in q:
#                             return {node, child}
#                         else:
#                             q.append(child)
#                     else:
#                         continue
#
#         redundants = []
#         for root in conns:
#             queue = [root]
#             res = bfs(root, queue)
#             if res not in redundants:
#                 redundants.append(res)
#
#         for edge in edges[::-1]:
#             if set(edge) in redundants:
#                 return edge


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantConnection([[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]))
