#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_list = head
        l = 0
        while head:
            l += 1
            head = head.next
        p = 0
        while result_list:
            if p == int(l/2):
                return result_list
            p += 1
            result_list = result_list.next