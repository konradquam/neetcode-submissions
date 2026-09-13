class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        substring_map = {}
        start_index = 0
        output = 0
    
        for index, char in enumerate(s):
            if char in substring_map.keys():
                while start_index < substring_map[char]:
                    substring_map.pop(s[start_index])
                    start_index += 1
                substring_map[char] = index
                start_index += 1
            else:
                substring_map[char] = index
                if len(substring_map) > output:
                    output = len(substring_map)
        
        return output
