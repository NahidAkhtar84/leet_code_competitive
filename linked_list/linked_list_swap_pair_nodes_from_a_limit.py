# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        if left >= right:
            return head
        
        prevx = prevy = None
        cpy_head = currx = curry = head
        
        pointer1 = 1
        pointer2 = 1
        
        while cpy_head:
            if pointer1 < left:
                prevx = currx
                currx = currx.next
                pointer1 += 1
                
            if pointer2 < right:
                prevy = curry
                curry = curry.next
                pointer2 +=1
                
            cpy_head = cpy_head.next
            
        # If either left or right is not present, nothing to do
        if currx == None or curry == None:
            return head
            
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
        
        head = self.reverseBetween(head, left+1, right-1)
        return head