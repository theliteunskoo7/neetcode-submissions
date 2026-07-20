class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i=0; j=len(s)-1
        while i < len(s):
            if j<i or j==i:
                break
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                print(s[i],s[j])
                if s[i]!=s[j]:
                    return False
                else:
                    i+=1
                    j-=1
        return True
                


        