class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        existing_Ones = s.count("1")
        n = len(s)

        zero_counts = []
        i = 0
        while i<n:
            if s[i] == '0':
                zero_count = 0
                while i<n and s[i] == '0':
                    zero_count += 1
                    i += 1
                zero_counts.append(zero_count)
            else: i += 1
        
        max_sum = 0
        for i in range(len(zero_counts) - 1):
            max_sum = max(max_sum, zero_counts[i] + zero_counts[i+1])
        
        return max_sum + existing_Ones

