class Solution:
    def isPalindrome(self, strs: str) -> bool:
        l, r = 0, len(strs) - 1

        while l < r:
            while l < r and not self.isalnum(strs[l]):
                l += 1

            while r > l and not self.isalnum(strs[r]):
                r -= 1

            if strs[l].lower() != strs[r].lower():
                return False

            l += 1
            r -= 1
        return True
    
    def isalnum(self, char: str) -> bool:
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )
