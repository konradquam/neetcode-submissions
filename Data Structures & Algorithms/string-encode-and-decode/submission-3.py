class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'fuckfuckfuck'

        encoded_string = '#FUCK#'.join(string for string in strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "fuckfuckfuck":
            return []
        decoded_strings = s.split('#FUCK#')
        return decoded_strings
