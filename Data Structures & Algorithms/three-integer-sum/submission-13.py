class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        op=[]
        nums=sorted(nums)
        while(i<=len(nums)-3):
            j=i+1
            d={}
            for j in range(i+1,len(nums)):
                sub= nums[i] + nums[j]
                if d.get(0-sub,0)==0:
                   d[nums[j]] = d.get(nums[j],0) + 1
                else:
                    if [nums[i],nums[j],(0-sub)] not in op:
                        op.append([nums[i],nums[j],(0-sub)])
                    d[nums[j]] = d.get(nums[j],0) + 1
            i+=1   
        return op
            

