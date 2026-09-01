class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict_h = {}
        for i in range(len(names)):
            dict_h[heights[i]]=names[i]
        
        return [v for k,v in sorted(dict_h.items(),reverse=True)]

        