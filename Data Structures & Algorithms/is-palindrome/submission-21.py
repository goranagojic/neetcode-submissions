class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaChar(c):
            if ord(c) in range(ord('A'), ord('Z')+1):
                return True
            if ord(c) in range(ord('a'), ord('z')+1):
                return True
            return False 
        
        def isNumeric(c):
            if ord(c) in range(ord('0'), ord('9')+1):
                return True
            return False
        
        i, j = 0, len(s) - 1
        while i < j:
            # if not (isAlphaChar(s[i]) or isNumeric(s[i])):
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True