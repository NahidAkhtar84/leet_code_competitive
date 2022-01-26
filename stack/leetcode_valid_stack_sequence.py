class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res_stack = []
        pointer1 = pointer2 = 0
        
        while pointer1 < len(pushed) or pointer2 < len(popped):
            if res_stack and res_stack[-1] == popped[pointer2]:
                pointer2 += 1
                res_stack.pop()
            elif pointer1 < len(pushed):
                res_stack.append(pushed[pointer1])
                pointer1 +=1
            else:
                break
                
        if len(res_stack) == 0:
            return True
        else:
            return False