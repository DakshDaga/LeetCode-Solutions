class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        curr, time = 0, 0
        for next in requests:
            time += abs(curr-next)
            curr = next
        return time