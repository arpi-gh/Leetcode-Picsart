class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def rotateRight(head: ListNode, k: int) -> ListNode:
    if head is None:
        return ListNode()

    length = 1
    current = head
    while current.next is not None:
        length += 1
        current = current.next

    if length - k == 0:
        return head
    elif k > length:
        end = length - (k % length)
    else:
        end = length - k

    current.next = head
    current = head
    for i in range(1, end):
        current = current.next
    head = current.next
    current.next = None
    return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

n8 = ListNode(8)

ls = [n1, n2, n3, n4, n5, n6]
h = rotateRight(n1, 4)

rotated = []
rotated.append(h)
while h.next is not None:
    h = h.next
    rotated.append(h)
print(rotated)
