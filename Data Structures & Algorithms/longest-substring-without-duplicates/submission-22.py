class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = 0
        r, l = 0, 0
        window = set()

        while r < len(s):
            # check if curr char is dup
            c = s[r]
            # yes
            # calculate max len of curr sequence, move l
            while c in window:
                window.remove(s[l])
                l += 1

            window.add(c)
            r += 1
            n = max(n, r - l)
            
        return n