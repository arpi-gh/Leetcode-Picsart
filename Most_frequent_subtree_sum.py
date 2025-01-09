class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def __init__(self):
        self.sum_records = {}

    def findFrequentTreeSum(self, root: TreeNode):
        if not root:
            return

        def record_sums(cur_sum):
            if cur_sum in self.sum_records:
                self.sum_records[cur_sum] += 1
            else:
                self.sum_records[cur_sum] = 1

        def dfs(root):
            if not root:
                return 0

            sum_left = dfs(root.left)
            sum_right = dfs(root.right)

            sum_whole = root.val + sum_left + sum_right

            record_sums(sum_whole)

            return sum_whole

        dfs(root)
        result = []
        max_count = 0
        for key in self.sum_records.keys():
            if self.sum_records[key] > max_count:
                result = [key]
                max_count = self.sum_records[key]
            elif self.sum_records[key] == max_count:
                result.append(key)

        return result


if __name__ == '__main__':
    n1 = TreeNode(5)
    n2 = TreeNode(2)
    n3 = TreeNode(-3)

    n1.left = n2
    n1.right = n3

    sol = Solution()
    print(sol.findFrequentTreeSum(n1))
