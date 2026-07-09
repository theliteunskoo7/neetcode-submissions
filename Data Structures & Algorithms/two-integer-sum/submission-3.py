class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        c=[]
        for i in range(len(nums)):
            if(d.get(target-nums[i])):
                return [int(d.get(target-nums[i])),i]
            d[nums[i]] = str(i)



        