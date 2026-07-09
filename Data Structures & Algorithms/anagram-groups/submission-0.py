class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        op=[]
        for x in strs:
            key = "".join(sorted(x))
            if(key in d):
                d[key].append(x)
            else:
                d[key] = [x]
        for k,v in d.items():
            op.append(v)
        return op 
