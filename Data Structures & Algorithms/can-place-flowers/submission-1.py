class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        extended = [0] + flowerbed + [0]
        space = 0
        for i in range(1,len(extended)-1):
            if extended[i-1] == 0 and extended[i] == 0 and extended[i+1] == 0:
                extended[i] = 1
                space += 1
            
        return n<=space

            
            
