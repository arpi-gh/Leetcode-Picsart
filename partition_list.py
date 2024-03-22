class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def partition(head: ListNode, x: int) -> ListNode:
    dummy = False
    current = head
    prev = ListNode()
    tmp = None
    while current.val < x and current.next is not None:
        tmp = current  # Save the previous value
        current = current.next
    pointer = current
    if tmp is not None:
        prev = tmp
    else:
        head = prev
        head.next = current
        dummy = True
    connection = current
    current = current.next
    while current is not None:
        if current.val < x:
            connection.next = current.next
            prev.next = current
            current.next = pointer
            prev = current
            current = connection.next
        else:
            connection = current
            current = current.next
            connection.next = current
    if dummy:
        head = head.next
    cur = head
    linked_list = []
    while cur is not None:
        linked_list.append(cur)
        cur = cur.next
    print(linked_list)
    return head


# [1,4,3,2,5,2]


n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(0)
n5 = ListNode(5)
n6 = ListNode(2)

# n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

print(partition(n1, 0))
