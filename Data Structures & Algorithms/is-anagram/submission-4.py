class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        d1,d2={},{}
        for a in s:
            d1[a] = d1.get(a,0)+1
        for b in t:
            d2[b] = d2.get(b,0)+1
        for x in d1:
            if(d1.get(x) != d2.get(x)):
                return False
        return True


        