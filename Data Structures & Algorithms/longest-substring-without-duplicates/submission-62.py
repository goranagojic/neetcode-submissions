class Solution:
    def lengthOfLongestSubstringBf(self, s: str) -> int:
        # input - string s having printable ascii chars
        # find the longest substring without duplicates

        # brute force
        # 15 min
        if not s:
            return 0

        max_len = 0
        l = 0
        for i in range(0, len(s)):
            window = set()
            l = 0
            for j in range(i, len(s)):
                if s[j] in window:
                    break
                window.add(s[j])
                l += 1
            max_len = max(max_len, l)

        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        r, l = 0, 0
        window = dict()
        max_len = 0
        while r < len(s):
            # while curr char not in window, move right
            while r < len(s) and window.get(s[r], -1) < l:
                window[s[r]] = r
                print(f"c = {s[r]}, window = {window}, l = {l}")
                r += 1

            # when it is
            # update result
            max_len = max(max_len, r - l)
            print(f"r, l = {r}, {l}, s = {s[l:r]}")
            if r < len(s): # if prev loop ended on second condition
                l = window[s[r]] + 1
                window[s[r]] = r

            r += 1
        
        return max_len