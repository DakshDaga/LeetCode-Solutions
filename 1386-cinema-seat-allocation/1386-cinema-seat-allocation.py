class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            reserved.setdefault(row, set()).add(seat)
        
        empty_rows = n - len(reserved)
        ans = 2 * empty_rows

        for seats in reserved.values():
            left = not seats & {2,3,4,5}
            middle = not seats & {4,5,6,7}
            right = not seats & {6,7,8,9}

            if left and right: ans += 2
            elif left or right or middle: ans += 1
        

        return ans
