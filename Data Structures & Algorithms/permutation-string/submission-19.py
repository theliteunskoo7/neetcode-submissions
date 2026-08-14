class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        for i in s1:
            d[i] =d.get(i,0)+1
        n=len(s1)
        m=len(s2)
        i=0
        e=d.copy()
        count=0
        l=0
        while i<m:
            if s2[i] not in e:
                l=i+1
                e=d.copy()
                count=0
                i+=1
            else:
                if e[s2[i]]!=0:
                    e[s2[i]]-=1
                    count+=1
                    if count==n:
                        return True
                    i+=1
                else:
                    e[s2[l]] = e.get(s2[l],0)+1
                    l+=1
                    if count>0:
                        count-=1
        return False


                





        