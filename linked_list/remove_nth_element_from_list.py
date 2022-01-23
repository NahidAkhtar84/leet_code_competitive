# Time Complexity O(N)
# Space Complexity O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        t_head = head
        length = 1
        while t_head:
            length += 1
            t_head = t_head.next
            
        m = 1
        res_list = ListNode(0)
        res_list.next = head
        prev = res_list
        curr = head
    
        while curr:
            if (length - m) == n:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            m += 1
                
        return res_list.next