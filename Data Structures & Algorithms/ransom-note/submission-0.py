class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_m = Counter(magazine)
        cnt_r = Counter(ransomNote)

        for char in ransomNote:
            if cnt_r[char] > cnt_m[char]:
                return False
        return True