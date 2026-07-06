class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        a1=list(a)
        print(a1)
        if sorted(a1)==sorted(nums):
            return bool(0)
        return bool(1)