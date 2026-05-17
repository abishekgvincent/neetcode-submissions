class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        end=len(s)-1
        for start in range(len(s)):
            if not s[start].isalnum():
                continue
            while (not s[end].isalnum()):
                end-=1
            if s[start]==s[end]:
                end-=1
            else:
                return False
        return True