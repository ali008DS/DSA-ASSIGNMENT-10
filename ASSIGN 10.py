class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_circular(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
