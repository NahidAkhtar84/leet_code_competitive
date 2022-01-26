# Definition for singly-linked list.
# Convert linked list to array, swap element and finally convert array to linked list 
# Time complexity: O(N)
# Space Complexity O(N)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        temp = arr[-k]
        arr[-k] = arr[k-1]
        arr[k-1] = temp
        res_list = swap = ListNode(0)
        for i in arr:
            res_list.next = ListNode(i)
            res_list = res_list.next
            
        return swap.next
               
                
            