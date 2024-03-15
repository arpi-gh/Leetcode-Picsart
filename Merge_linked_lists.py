class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def mergeTwoLists(list1: ListNode, list2: ListNode) -> [ListNode]:
    dummy = ListNode()
    current = list1
    compared = list2
    merged = []

    if current is None:
        return compared
    elif compared is None:
        return current
    else:
        if current.val <= compared.val:
            dummy.next = current
        else:
            dummy.next = compared
            current, compared = compared, current
        merged.append(dummy.next)
        # print(merged)

    end = False
    while not end:
        if current.next is None:
            if compared is not None:
                current.next = compared
                current = compared
                merged.append(current)
                while current.next is not None:
                    current = current.next
                end = True
            # print(merged)
            return dummy.next
        if current.next.val <= compared.val:
            current = current.next
            merged.append(current)
            # print(merged)
        else:
            tmp = current.next
            current.next = compared
            merged.append(compared)
            current = compared
            compared = tmp


n1 = ListNode(1)
n2 = ListNode(2)
n4 = ListNode(4)
n1.next = n2
n2.next = n4

m1 = ListNode(1)
m3 = ListNode(3)
m4 = ListNode(4)

m1.next = m3
m3.next = m4

ls1 = n1
ls2 = m1


print(mergeTwoLists(ls1, ls2))