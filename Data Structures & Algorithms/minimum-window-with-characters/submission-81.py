class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s - string, t - string
        # return a minimal len substring of s containing all chars in t
        # substring must contain all chars from t, but extra chars are allowed


        # The idea:
        # use variable size sliding window to move through s in order to find the shortest substring
        # use hashmaps to track chars in window, but only for chars that also appear in t
        # use idea of tracking matches to avoid complete hashmap comparison every time window hashmap is updated
        # use the following rules to manipulate a sliding window
        #   - while having less matches then expected - grow the window to the right
        #   - while having enoguh matches, shringk the window from the left
        # can be implemented as two squential while loops that repeat grow-shrink phases while r does not reach the end of the string
        # every time you shrink the string, try to update shortest window info
        # ofc, track shortest window inf through r and l pointers, len also, because you will need to return a substring at the end
        # handle edge cases like empty t, s shorter than t

        if not t or len(s) < len(t):
            return ""

        s_map, t_map = dict(), dict()
        
        # init t_map, char count in t
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
            s_map[c] = 0

        # init s_map on the first window
        for i in range(0, len(t)):
            c = s[i]
            if c in s_map:
                s_map[c] += 1

        # how many matches are there
        matches, expected = 0, len(t_map)
        for c in t_map.keys():
            if s_map[c] >= t_map[c]:
                matches += 1

        # have matches == expected
        l, r = 0, len(t)
        l_s, r_s, s_len = -1, -1, float("infinity") # r_s exclusive

        # the check is needed because i start from a precomputed fixed-size window
        # it can be avoided if i let the window grow from 0 size
        if matches == expected:
            l_s, r_s = 0, r
            s_len = r_s - l_s

        while r < len(s):
            # expand window while some characters are missing
            while r < len(s) and matches != expected:
                c = s[r]
                if c in s_map:
                    s_map[c] += 1
                    if s_map[c] == t_map[c]:
                        matches += 1
                r += 1

            # reduce window while matches are satisfied
            while l <= r and matches == expected:
                
                # update shortest substring
                if r - l < s_len:
                    l_s, r_s = l, r
                    s_len = r_s - l_s

                # then remove current character
                c = s[l]
                if c in s_map:
                    s_map[c] -= 1
                    if s_map[c] + 1 == t_map[c]:
                        matches -= 1
                l += 1

        return s[l_s:r_s] if s_len != float("infinity") else ""