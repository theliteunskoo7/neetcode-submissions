class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        e={}
        for i in s1:
            d[i] = d.get(i,0) + 1
        n=len(s1)
        count=0
        for j in range(len(s2)):
            if j<n:
                e[s2[j]] = e.get(s2[j],0) + 1
            else:
                e[s2[j-n]] = e[s2[j-n]]-1
                if e.get(s2[j-n],0)==0:
                    del e[s2[j-n]]
                e[s2[j]] = e.get(s2[j],0) + 1
            if e==d:
                return True
            j+=1
        return False





                





        