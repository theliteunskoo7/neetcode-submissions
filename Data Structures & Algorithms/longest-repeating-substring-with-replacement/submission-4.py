class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        maxf=0
        ws=0
        res=0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            maxf = max(d[s[i]],maxf)
            while i-ws+1-maxf>k:
                d[s[ws]]-=1
                ws+=1
            res=max(res,i-ws+1)
        return res
