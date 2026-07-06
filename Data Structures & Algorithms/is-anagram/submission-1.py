class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        for i in s:
            x=t.find(i)
            if(x==-1):
                return False
            t=t[:x] + t[x+1:]

        return True

        