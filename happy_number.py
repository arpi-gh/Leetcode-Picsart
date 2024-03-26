class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def isHappy(n: int) -> bool:
    pointer = head = ListNode(n)
    res = digits_squared(n)
    while res != 1:
        current = head
        while current.next is not None:
            if current.val == res:
                pointer.next = current
                return False
            else:
                current = current.next
        pointer.next = ListNode(res)
        res = digits_squared(res)
        pointer = pointer.next
    return True


def digits_squared(n: int) -> int:
    result = 0
    while n != 0:
        result += ((n % 10) ** 2)
        n //= 10
    return result



print(isHappy(25))