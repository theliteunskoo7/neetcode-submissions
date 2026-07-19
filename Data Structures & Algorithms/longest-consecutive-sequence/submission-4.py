class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        for a in nums:
            d[a] = d.get(a,{a})
            if d.get(a-1,0)!=0:
                d[a-1].add(a)
                d[a].add(a-1)
            if d.get(a+1,0)!=0:
                d[a+1].add(a)
                d[a].add(a+1)
        for a in nums:
            if d.get(a-1,0)!=0:
                t=d[a]
                d[a] = d[a] | d[a-1] 
                d[a-1]=d[a-1] | t
                
            if d.get(a+1,0)!=0:
                t=d[a]
                d[a] = d[a] | d[a+1]
                d[a+1] = d[a+1] | t
        max=0
        print(d)
        for a in d:
            x = len(set(d[a]))
            if x>max:
                max=x
        return max
            

            
        
