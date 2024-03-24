class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


def insertionSortList(head: ListNode) -> ListNode:
    pointer = ListNode(0)
    pointer.next = head  # Create a pointer that points to the head
    current = head  # start with the head
    while current.next is not None:
        node = current.next    # keep the value of the node that's being compared
        if node.val < current.val:
            start = pointer  # start from the pointer
            while start is not current:
                if start.next.val > node.val:
                    current.next = current.next.next  # link the nodes on both sides
                    node.next = start.next
                    start.next = node
                    break
                start = start.next
        else:
            current = current.next
    cur = head
    linked_list = []
    while cur is not None:
        linked_list.append(cur)
        cur = cur.next
    print(linked_list)
    return pointer.next


n1 = ListNode(-1)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(6)
n5 = ListNode(0)
n6 = ListNode(5)
n7 = ListNode(2)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

print(insertionSortList(n1))
