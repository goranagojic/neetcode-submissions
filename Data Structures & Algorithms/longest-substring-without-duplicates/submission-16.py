class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        dupes = set()
        for i in range(0, len(s)):
            dupes = set()
            for j in range(i, len(s)):
                c = s[j]
                if c in dupes:
                    max_len = max(max_len, j - i + 1)
                    break
                dupes.add(c)

        return max_len


    def lengthOfLongestSubstringDict(self, s: str) -> int:

        if len(s) in [0, 1]:
            return len(s)

        # define window (left, right)
        l, r = 0, 0
        # hashmap to check duplicates (char: index)
        window = dict()
        # n - s len, max_len
        n, max_len = 0, 0

        # iterate through the array
        while r < len(s):
            # r = l
            # check if the char is in dupes
            c = s[r]
            if c in window: # yes
                # get the index of previous appearance
                prev_c_idx = window[c]
                if  prev_c_idx >= l:            # belongs to this substring?
                    max_len = max(max_len, n)   # update max_len
                    n_delta = (prev_c_idx + 1) - l
                    n = n - n_delta + 1         # +1 because found duplicate is valid element of a substring
                    l = prev_c_idx + 1          # move left boundary
                else: # no: idx < right
                    n += 1
                window[c] = r               # update hashmap
            else: # no
                # add to hashmap
                window[c] = r
                # move right
                n += 1
            r += 1

        max_len = max(max_len, n)
                    
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0, 1]:
            return len(s)

        l, r = 0, 0
        window = set()
        n, max_len = 0, 0

        while r < len(s):
            c = s[r]
            if c in window:
                max_len = max(max_len, n)
                while c in window:
                    window.remove(s[l])
                    l += 1
                    n -= 1
            n += 1
            r += 1
            window.add(c)

        max_len = max(max_len, n)

        return max_len
