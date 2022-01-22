# simple solution
# Time Complexity: O(2N)
# Space Complexity O(N)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        t_head = head
        while t_head:
            l += 1
            t_head = t_head.next
        res_list = ListNode(0)
        res_list.next = head
        prev = res_list
        curr = head
        
        p = 0
        while curr:
            if p == l//2:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            p +=1
        return res_list.next