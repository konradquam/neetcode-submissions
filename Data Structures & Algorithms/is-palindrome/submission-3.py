class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) -1

        while first < last:
            while first < len(s) and not s[first].isalnum():
                first += 1
            while last >= 0 and not s[last].isalnum():
                last -= 1
            if first > last:
                break
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        
        return True