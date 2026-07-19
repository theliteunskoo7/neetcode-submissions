class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        for a in nums:
            d[a] = 1
        for a in d:
            if d.get(a-1,0):
                d[a] = d[a-1] + 1
            if d.get(a+1,0):
                d[a+1] = d[a] + 1
        for a in d:
            if d.get(a-1,0):
                if d[a]-d[a-1] != 1:
                    d[a] = d[a-1] + 1
            if d.get(a+1,0):
                if d[a+1]-d[a] != 1:
                    d[a+1] = d[a] + 1
        if len(d) == 0:
            return 0
        else:
            return max(d.values())