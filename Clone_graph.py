class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f'node<{self.val}>'


class Solution(object):
    def __init__(self):
        self.created = {}

    def cloneGraph(self, node):
        if node is None:
            return
        else:
            return self.dfs(node)

    def dfs(self, node):
        if node.val not in self.created:
            self.created[node.val] = Node(node.val)

        for neighbor in node.neighbors:
            if neighbor.val not in self.created:
                n = self.dfs(neighbor)
                self.created[node.val].neighbors.append(n)
            else:
                self.created[node.val].neighbors.append(self.created[neighbor.val])

        return self.created[node.val]


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n4]
    n3.neighbors = [n1, n4]
    n4.neighbors = [n2, n3]
    sol = Solution()
    print(sol.cloneGraph(n1))

