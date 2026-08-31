# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        pos = 1
        criticals = []
        while(curr.next.next):
            if(curr.next.val > curr.val and curr.next.val > curr.next.next.val):
                criticals.append(pos)
            if(curr.next.val < curr.val and curr.next.val < curr.next.next.val):
                criticals.append(pos)
            
            pos += 1
            curr = curr.next
        
        if(len(criticals) > 1):
            maxDist = criticals[-1] - criticals[0]
            minDist = 1e9
            for i in range(len(criticals)-1):
                minDist = min(minDist, criticals[i+1] - criticals[i])
            
            return [minDist, maxDist]
        
        return [-1, -1]