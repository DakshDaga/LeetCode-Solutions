class Solution:
    class Node:
        def __init__(self, leftChr=0, rightChr=0, pref=0, suff=0, maxLen=0):
            self.leftChr = leftChr
            self.rightChr = rightChr
            self.pref = pref
            self.suff = suff
            self.maxLen = maxLen
        

    def buildSegTree(self, i, l, r, s):
        if(l == r):
            self.segTree[i] = self.Node(s[l], s[l], 1, 1, 1)
            return

        mid = l + (r-l)//2
        self.buildSegTree(2*i + 1, l, mid, s)
        self.buildSegTree(2*i + 2, mid+1, r, s)
        
        self.segTree[i] = self.merge(self.segTree[2*i + 1], self.segTree[2*i + 2], mid-l+1, r-mid)

    def merge(self, L, R, leftLen, rightLen):
        res = self.Node()

        res.leftChr, res.rightChr = L.leftChr, R.rightChr

        res.pref = L.pref
        if(L.pref == leftLen and L.rightChr == R.leftChr): res.pref = L.pref + R.pref

        res.suff = R.suff
        if(R.suff == rightLen and R.leftChr == L.rightChr): res.suff = R.suff + L.suff

        res.maxLen = max(L.maxLen, R.maxLen)
        if(L.rightChr == R.leftChr): res.maxLen = max(res.maxLen, L.suff + R.pref)

        return res

    def updateSegTree(self, i, l, r, ch, pos):
        if(l == r):
            self.segTree[i] = self.Node(ch, ch, 1, 1, 1)
            return

        mid = l + (r-l)//2
        if pos <= mid:
            self.updateSegTree(2*i + 1, l, mid, ch, pos)
        else:
            self.updateSegTree(2*i +2, mid+1, r, ch, pos)
        
        self.segTree[i] = self.merge(self.segTree[2*i + 1], self.segTree[2*i + 2], mid-l+1, r-mid)

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        self.segTree = [self.Node() for _ in range(4*n)]
        self.buildSegTree(0, 0, n-1, s)

        ans = []

        for ch, pos in zip(queryCharacters, queryIndices):
            self.updateSegTree(0, 0, n - 1, ch, pos)
            ans.append(self.segTree[0].maxLen)

        return ans