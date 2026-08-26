class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict_s = {}
        for num in arr1:
            if num in dict_s:
                dict_s[num] += 1
            else:
                dict_s[num] = 1
        
        sort_dict = dict(sorted(dict_s.items()))
        temp = []
        for num in arr2:
            temp += [num]*sort_dict[num]
            sort_dict.pop(num)
        
        for index in sort_dict:
            temp += [index]*sort_dict[index]
        
        
        return temp
        