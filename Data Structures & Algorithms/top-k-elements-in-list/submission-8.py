class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        d1=defaultdict(list)
        c=0
        op=[]
        for i in nums:
            d[i] = d.get(i,0)+1
        for j in d:
            d1[d[j]].append(j)
        # count = sorted(d1.keys(),reverse=True)
        # for i in range(len(d1.keys())):
        #     op = op + d1[count[i]]
        for i in range(len(nums),0,-1):
            op.extend(d1[i])



        return op[:k]


        
        


        