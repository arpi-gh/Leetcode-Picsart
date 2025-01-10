class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'

    def __lt__(self, other):
        if self.val < other.val:
            return True
        return False

    def __gt__(self, other):
        if self.val > other.val:
            return True
        return False




# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         ...


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)

    ls = [n2, n1]
    ls.sort()
    print(ls)

