class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        window=0
        for i in range(len(s)):
            exist = d.get(s[i],-1)
            if exist==-1:
                d[s[i]] = i
                r = i
            elif exist!=-1:
                if d[s[i]]>=l:
                    l = d[s[i]] + 1
                    d[s[i]] = i 
                    r=i
                else:
                    d[s[i]] = i
                    r=i
            window = max(window,r-l+1)
            # print(i,exist,l,r)
        return window



