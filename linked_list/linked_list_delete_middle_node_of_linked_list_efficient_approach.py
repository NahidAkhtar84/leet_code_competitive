# Time Complexity: O(N)
# Space Complexity O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        slow_p = fast_p = head
        while fast_p and fast_p.next:
            prev = slow_p
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            
        prev.next = slow_p.next
        return head