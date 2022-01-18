
"""
FLOYDS CYCLE FINDING ALGORITHM --> Fastest
"""

#! Approach: This is the (fastest) method and has been described below:  

#! Traverse linked list using two pointers.
#! Move one pointer(slow_p) by one and another pointer(fast_p) by two.
#! If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.

# Time Complexity O(N)
# Space Complexity O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            
            if slow_p == fast_p:
                return True
        return False