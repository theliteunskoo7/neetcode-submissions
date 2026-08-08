class Solution:
    def maxArea(self, heights: List[int]) -> int:
        op=0
        n=len(heights)
        i = 0
        j = n-1
        while i<j:
            b = (j-i) * min(heights[j],heights[i])
            op = max(op,b)
            if (heights[i]>heights[j]):
                j-=1
            else:
                i+=1
        return op