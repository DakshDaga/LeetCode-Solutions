class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique = set()
        for i in range(100, 1000, 2):
            d = [int(x) for x in str(i)]
            
            if all(d.count(x) <= digits.count(x) for x in d):
                unique.add(i)
        return len(unique)