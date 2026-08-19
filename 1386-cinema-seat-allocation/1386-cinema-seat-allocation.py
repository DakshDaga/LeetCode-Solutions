class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {row: [] for row,_ in reservedSeats}

        for row, seat in reservedSeats:
            reserved[row].append(seat)
        
        ans = 0
        for seats in reserved.values():
            left = not any(seat in seats for seat in [2,3,4,5])
            middle = not any(seat in seats for seat in [4,5,6,7])
            right = not any(seat in seats for seat in [6,7,8,9])

            if left and right: ans += 2
            elif left or right or middle: ans += 1
        
        empty_rows = n - len(reserved)
        ans += 2 * empty_rows

        return ans
