
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        t_head = head
        length_count = 0
        while t_head:
            length_count += 1
            t_head = t_head.next
            
        prevx = prevy = None
        currx = curry = head
        
        pointer1 = 1
        pointer2 = 0
        
        while pointer1 < k:
            pointer1 += 1
            prevx = currx
            currx = currx.next
            
        while pointer2 < length_count - k:
            pointer2 += 1
            prevy = curry
            curry = curry.next
        if prevx != None:
            prevx.next = curry
        else:
            head = curry
        if prevy != None:
            prevy.next = currx
        else:
            head = currx
        
        temp = curry.next
        curry.next = currx.next
        currx.next = temp
        
        return head
            
                
            
        
            
               
                
            