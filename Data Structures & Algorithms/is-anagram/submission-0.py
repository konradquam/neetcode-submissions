class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for item in s:
            if item in s_map.keys():
                s_map[item] += 1
            else:
                s_map[item] = 1
        
        for item in t:
            if item in t_map.keys():
                t_map[item] += 1
            else:
                t_map[item] = 1
        
        for key, val in s_map.items():
            if key not in t_map.keys() or t_map[key] != val:
                return False
        return True
        