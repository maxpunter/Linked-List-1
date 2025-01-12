# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        valid = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                valid = True
                break

        if not valid: return None
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow