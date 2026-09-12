class Solution:
    
    class Node:
        def __init__(self):
            self.score = 0
            self.idxs = []

    n = 0
    nextIdx = [-1] * n
    memo = {}

    def get_next_idx(self, intervals, i):
        l, r = i, len(intervals)-1
        end = intervals[i][1]
        res = self.n
        while(l <= r):
            mid = l + (r-l)//2
            if intervals[mid][0] > end:
                res = mid
                r = mid-1
            else: l = mid+1
        
        return res


    def solve(self, intervals, i, k):
        if(k == 0 or i >= self.n):
            return self.Node()

        if (i, k) in self.memo: return self.memo[(i, k)]

        skip = self.solve(intervals, i+1, k)

        weight = intervals[i][2]
        idx = intervals[i][3]
        j = self.nextIdx[i]
        temp = self.solve(intervals, j, k-1)

        take = self.Node()
        take.score = temp.score + intervals[i][2]
        take.idxs = temp.idxs + [idx]
        take.idxs.sort()

        if skip.score > take.score:
            result = skip
        elif take.score > skip.score:
            result = take
        else:
            result = skip if skip.idxs < take.idxs else take
        
        self.memo[(i, k)] = result
        return result

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        self.memo = {}
        for i, interval in enumerate(intervals):
            interval.append(i)
        
        intervals.sort()
        self.n = len(intervals)
        self.nextIdx = [-1] * self.n
        for i in range(self.n):
            self.nextIdx[i] = self.get_next_idx(intervals, i)

        K = 4
        ans = self.solve(intervals, 0, K)
        return ans.idxs
        