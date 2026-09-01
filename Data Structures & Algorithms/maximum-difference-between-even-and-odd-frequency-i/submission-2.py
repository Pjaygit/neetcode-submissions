class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odds = []
        evens = []

        for val in cnt.values():
            if val % 2 != 0:
                odds.append(val)
            else:
                evens.append(val)
        
        return max(odds)-min(evens)

            
        