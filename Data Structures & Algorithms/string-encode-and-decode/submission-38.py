class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(a)}#{a}" for a in strs)

    def decode(self, s: str) -> List[str]:
        op = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # find end of the length field
            l = int(s[i:j])
            op.append(s[j+1 : j+1+l])
            i = j + 1 + l
        return op