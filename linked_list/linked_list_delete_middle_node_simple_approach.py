#Time Complexity O(N)
# Space Complexity O(1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        t_head = cpy_head = head
        if head == None or head.next == None:
            return None
        while t_head:
            l += 1
            t_head = t_head.next
        
        middle_node_index = l//2
        while middle_node_index > 1:
            head = head.next
            middle_node_index -= 1
        head.next = head.next.next
        return cpy_head
        