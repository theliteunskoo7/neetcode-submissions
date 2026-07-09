class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        op=[]
        for x in strs:
            a = [0]*26
            for y in x:
                a[ord(y)-ord('a')]+=1
            d[tuple(a)].append(x)

        print(d)
        return list(d.values()) 
