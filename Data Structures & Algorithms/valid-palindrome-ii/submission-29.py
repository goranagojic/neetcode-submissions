class Solution:
    def validPalindromeIncorrect(self, s: str) -> bool:
        # NOTICE: This solution is incorrect when it is both true that s[i+1]==s[j] and s[i]==s[j-1] because it opts for one option that
        # later might lead to the incorrect result!
        # check palindrome
        i, j, skips = 0, len(s)-1, 0
        while i < j:
            print(f"i={i}, j={j}")
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                # look forward
                if s[i+1] == s[j] and i+1 <= j:
                    j, skips = j + 1, skips + 1
                    print(f"Skipped {s[i]}")
                elif s[i] == s[j - 1] and i <= j-1:
                    i, skips = i - 1, skips + 1
                    print(f"Skipped {s[j]}")
                else:
                    return False

            i, j = i + 1, j - 1

        print(f"skips {skips}")

        if skips > 1:
            return False

        return True

    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s: str) -> bool:
            i, j = 0, len(s)-1
            while i < j:
                lc, rc = s[i], s[j]
                if not lc.isalnum():
                    i += 1
                    continue
                if not rc.isalnum():
                    j -= 1
                    continue
                if lc.lower() != rc.lower():
                    return False
                i, j = i + 1, j - 1

            return True

        i, j = 0, len(s)-1 
        while i < j:
            if s[i] != s[j]:
                left = s[:i] + s[i+1:]
                print(left)
                right = s[:j] + s[j+1:]
                print(right)
                return is_palindrome(left) or is_palindrome(right)
            i, j = i + 1, j - 1

        return True

