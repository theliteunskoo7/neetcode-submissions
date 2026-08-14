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
                if e[s2[j]] == d.get(s2[j],0):
                    count = count + e[s2[j]]
                    if count == n:
                        return True
            else:
                if d.get(s2[j-n],0)>0:
                    if e[s2[j-n]] == d.get(s2[j-n],0):
                        count-=1
                    e[s2[j-n]]-=1
                e[s2[j]] = e.get(s2[j],0) + 1
                if e[s2[j]] == d.get(s2[j],0):
                    count = count + e[s2[j]]
                    if count == n:
                        return True
            j+=1
            print(e)
        return False





                





        