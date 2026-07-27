class Solution:
    def maxArea(self, heights: List[int]) -> int:
        op=0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                x = min(heights[i],heights[j])
                y = j-i
                if x*y>op:
                    op=x*y
        return op

        