class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        t = s.split()
        r = t[len(t)-1]
        return len(r)
        
        