from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s - string, t - string
        # return a minimal len substring of s containing all chars in t
        # substring must contain all chars from t, but extra chars are allowed

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
        l, r = 0, len(t) - 1
        l_s, r_s, s_len = -1, -1, float("infinity") # r_s exclusive

        if matches == expected:
            l_s, r_s = 0, r + 1
            s_len = r_s - l_s

        while r < len(s) - 1:
            # expand window while some characters are missing
            while r < len(s) - 1 and matches != expected:
                # move to the next c (r += 1)
                r += 1
                c = s[r]
                # if char not in t, just move to the next
                if c not in s_map:
                    continue
                # if yes, update s_map
                s_map[c] += 1
                # update matches
                if s_map[c] == t_map[c]:
                    matches += 1
                print(matches)
            print(f"Matches found. Substring: {s[l+1:r+1]}")

            # reduce window while matches are satisfied
            while l <= r and matches == expected:
                
                # update shortest substring
                if r - l + 1 < s_len:
                    l_s, r_s = l, r + 1
                    s_len = r_s - l_s

                # then remove current character
                c = s[l]
                if c in s_map:
                    s_map[c] -= 1
                    if s_map[c] + 1 == t_map[c]:
                        matches -= 1
                l += 1

        return s[l_s:r_s] if s_len != float("infinity") else ""



    def minWindow1(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        # count chars in t string
        t_map = dict()
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        print(f"t_map={t_map}")

        # count same chars in s string
        s_map = dict()
        for c in t:
            s_map[c] = 0

        for i in range(0, len(t)):
            c = s[i]
            if c in s_map:
                s_map[c] += 1

        # see how many matches are there in the first window (0, len(t))
        matches = 0
        for c in t:
            if s_map[c] == t_map[c]:
                matches += 1
        print(f"matches = {matches}")

        if matches == len(t):
            return s[:len(t)]

        # iterate through s, update match once you find the char from t
        # keep track of the shortest substring
        l, r = 0, len(t)
        l_shortest, r_shortest = 0, 10000
        k = len(t)
        while r < len(s):
            c = s[r]
            if c not in s_map:
                r += 1
            else:
                s_map[c] += 1
                if s_map[c] == t_map[c]:
                    matches += 1
                elif s_map[c] - 1 == t_map[c]:
                    matches -= 1
                
                if matches == k:
                    # shorten as much as you can by removing all charactes not appearing at t
                    while s[l] not in s_map:
                         l += 1
                    print(f"after reduction: {s[l:r+1]}")
                    print(f"matches = {matches}")

                    # get current substring length
                    lens = r - l + 1
                    if r_shortest - l_shortest > lens:
                        l_shortest = l
                        r_shortest = r + 1
                        print(f"again {s[l_shortest:r_shortest]}")
                    s_map[s[l]] -= 1
                    l += 1 # exclude one t char
                    matches -= 1
                r += 1

        if r_shortest == 10000:
            return ""

        return s[l_shortest:r_shortest]        
                