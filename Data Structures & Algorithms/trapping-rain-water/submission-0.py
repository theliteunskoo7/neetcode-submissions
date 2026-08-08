class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        x=0
        y=0
        tot=defaultdict(list)
        open=True
        l=[0]*n
        r=[0]*n
        o=[0]*n
        left=0
        right=n-1
        for i in range(0,n):
            l[i] = left
            if height[i]>height[left]:
                left = i
        for j in range(n-1,-1,-1):
            r[j] = right
            if height[j]>=height[right]:
                right=j
        for i in range(0,n):
            o[i] = min(height[l[i]],height[r[i]]) - height[i]
            if o[i]<0:
                o[i]=0
        return sum(o)

            
            








        