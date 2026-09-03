class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even, odd = [], []
        for num in nums1:
            if(num % 2 == 0):
                even.append(num)
            else: odd.append(num)
        
        if(even and odd):
            diff = min(even) - min(odd)
            if diff < 1:
                return False
        
        return True