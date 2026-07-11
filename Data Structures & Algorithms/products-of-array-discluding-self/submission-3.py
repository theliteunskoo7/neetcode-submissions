class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        su=[1]*len(nums)
        op = []
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]
        for i in range(len(nums)-2,-1,-1):
            su[i] = nums[i+1] * su[i+1]
        for i in range(len(nums)):
            op.append(pre[i]*su[i])
        return op
        