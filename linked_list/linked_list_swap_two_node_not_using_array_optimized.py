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
        cpy_head = currx = curry = head
        
        pointer1 = 1
        pointer2 = 0
        
        while cpy_head:
            if pointer1 < k:
                prevx = currx
                currx = currx.next
                pointer1 +=1
            if pointer2 < length_count-k:
                prevy = curry
                curry = curry.next
                pointer2 +=1
            cpy_head = cpy_head.next
            
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
            
                
            
        
            
               
                
            