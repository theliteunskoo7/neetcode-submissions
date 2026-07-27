class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        op=[]
        nums = sorted(nums)
        i=0
        while(i<=len(nums)-3):
            j = i+1
            k = len(nums)-1
            while(j<k):
                if (nums[j] + nums[k] + nums[i]) == 0:
                    if [nums[j],nums[k], nums[i]] not in op:
                        op.append([nums[j], nums[k], nums[i]])
                    j = j + 1
                elif (nums[j] + nums[k] + nums[i]) > 0:
                    k = k-1
                elif (nums[j] + nums[k] + nums[i]) < 0:
                    j = j+1
            i+=1
        return op

