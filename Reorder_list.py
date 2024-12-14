class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


# Time Limit Exceeded
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         if not head.next or not head.next.next:
#             return
#
#         left = head
#         right = head.next
#         nodes = []
#
#         while right.next and right.next.next:
#             left = left.next
#             right = right.next.next
#
#         left = left.next
#         while left:
#             nodes.append(left)
#             left = left.next
#
#         nodes.reverse()
#         mid = len(nodes) - len(nodes) % 2
#
#         current = head
#         for i in range(mid):
#             print(f'{current} -> {current.next}')
#             if nodes[i] == current.next:
#                 break
#             tmp = current.next
#             current.next = nodes[i]
#             print(f'{current} -> {current.next}')
#             nodes[i].next = tmp
#             current = tmp
#
#         if mid % 2 == 1:
#             current.next = nodes[-1]
#
#         nodes[-1].next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head.next or not head.next.next:
            return

        left = head
        right = head.next

        while right.next and right.next.next:
            left = left.next
            right = right.next.next

        if right.next:
            right = right.next
            left = left.next

        head_2 = left.next
        left.next = None

        current = head_2
        next_node = current.next

        while next_node:
            pivot = next_node
            next_node = next_node.next
            pivot.next = current
            current = pivot

        head_2.next = None

        left = head
        right = current

        while left and right:
            l = left.next
            r = right.next
            left.next = right
            right.next = l
            left = l
            last = right
            right = r

        if left:
            last.next = left

        return head


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sol = Solution()
    sol.reorderList(n1)

    current = n1
    while current:
        print(current)
        current = current.next
