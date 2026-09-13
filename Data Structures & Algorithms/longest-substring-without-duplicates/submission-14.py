class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        substring_map = {}
        start_index = 0
        output = 0
    
        for index, char in enumerate(s):
            if char in substring_map.keys():
                if substring_map[char] + 1 >= start_index:
                    start_index = substring_map[char] + 1
                substring_map[char] = index
            else:
                substring_map[char] = index
            output = max(output, index-start_index+1)
        
        return output
