class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[]
        for i in range(len(nums)):
            product=1
            for j in (nums[:i]+nums[i+1:]):
                product*=j
            op.append(product)
        return op