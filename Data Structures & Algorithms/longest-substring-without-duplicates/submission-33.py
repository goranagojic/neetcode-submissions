class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input - string s having printable ascii chars
        # find the longest substring without duplicates

        # brute force
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

        max_len = max(max_len, l)

        return max_len
        
                