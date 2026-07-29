class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for st, end, seats in bookings:
            ans[st-1] += seats
            if end < len(ans): ans[end] -= seats
        
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]
        
        return ans