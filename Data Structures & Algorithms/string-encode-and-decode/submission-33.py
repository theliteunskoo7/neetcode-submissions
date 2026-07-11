class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        if len(strs)==0:
            return "emptylist"
        for a in strs:
            n = str(len(a))
            if len(n) ==1:
                n = "00"+n
            elif len(n) == 2:
                n ="0" + n
            s+=n + a
        return s 

    def decode(self, s: str) -> List[str]:
        op=[]
        i=0
        if s=="emptylist":
            return []
        while  i < len(s):
            l = int(s[i:i+3])
            stri = s[(i+3):(i+3+l)]
            op.append(stri)
            i = i + l + 3
        return op
        
