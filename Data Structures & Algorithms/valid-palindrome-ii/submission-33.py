class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str, i: int, j: int) -> bool:
            while i < j:
                lc, rc = s[i].lower(), s[j].lower()
                if not lc.isalnum():
                    i += 1
                    continue
                if not rc.isalnum():
                    j -= 1
                    continue
                if lc != rc:
                    return False
                i, j = i + 1, j - 1

            return True

        i, j = 0, len(s)-1 
        while i < j:
            if s[i] != s[j]: # just for the first missmatch
                return is_palindrome(s,i+1,j) or is_palindrome(s,i,j-1)
                # example
                #   "abbadc" - difference on i=0,j=5
                #   is_palindrome(s,i+1,j) - 1,5 -> bbadc
                #   is_palindrome(s,i,j-1) - 0,4 -> abbad
                # false
                # example
                #   "abbda" - missmatch on i=1,j=3
                #   is_palindrome(s,i+1,j) - 2,3 -> "bd"
                #   is_palindrome(s,i,j-1) - 1,2 -> "bb" T
            i, j = i + 1, j - 1

        return True
