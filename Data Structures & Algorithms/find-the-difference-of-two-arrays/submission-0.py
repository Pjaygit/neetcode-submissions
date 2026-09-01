class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        temp = []
        for num in nums1:
            if num not in nums2:
                if num not in temp:
                    temp.append(num)

        temp2 = []
        for num in nums2:
            if num not in nums1:
                if num not in temp2:
                    temp2.append(num)
        
        return [temp,temp2]