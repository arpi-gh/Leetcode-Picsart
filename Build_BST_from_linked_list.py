class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def sortedListToBST(self, head: ListNode):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root

        slow = head
        fast = head.next
        end = slow
        while fast.next and fast.next.next:
            end = slow
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            end = slow
            slow = slow.next
            fast = fast.next

        root = TreeNode(slow.val)
        start = slow.next
        end.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(start)

        return root


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    n8 = ListNode(8)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8

    sol = Solution()
    print(sol.sortedListToBST(n1))