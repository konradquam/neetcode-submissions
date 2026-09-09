class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        real_output = []

        for item in strs:
            sorted_string = "".join(sorted(item))
            if sorted_string in output.keys():
                output[sorted_string].append(item)
            else:
                output[sorted_string] = [item]
        for val in output.values():
            real_output.append(val)
        return real_output