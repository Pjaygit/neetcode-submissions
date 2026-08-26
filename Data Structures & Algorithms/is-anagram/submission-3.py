class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s,dict_t = {},{}
        for w in s:
            if w in dict_s:
                dict_s[w] += dict_s[w]
            else:
                dict_s[w] = 1
        
        for w in t:
            if w in dict_t:
                dict_t[w] += dict_t[w]
            else:
                dict_t[w] = 1
        
        return dict_s == dict_t
                 
            
