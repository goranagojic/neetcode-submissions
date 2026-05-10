from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def find_maxfreq(freqs):
            # this will be time complexity of O(26) because the assignment is limited to uppercase eng. chars
            maxf = -1
            for k, v in freqs.items():
                maxf = max(maxf, v)
            return maxf

        n = 0
        l, r = 0, 0
        freqs = dict()
        freqc = 0
        while r < len(s):
            c = s[r]
            freqs[c] = freqs.get(c, 0) + 1
            # update the character appearing most of the time in a substring
            freqc = max(freqc, freqs[c])
            # check if there are at most k characters to replace
            while (r - l + 1) - freqc > k:
                # correct the most frequent
                freqs[s[l]] -= 1
                freqc = find_maxfreq(freqs)
                l += 1
            n = max(n, r - l + 1)
            r += 1

        return n


    def characterReplacementIncorrect(self, s: str, k: int) -> int:
        count = dict()
        last_seen = dict()
        distance = dict()

        for i in range(len(s)):
            c = s[i]
            count[c] = count.get(c, 0) + 1
            if c in distance:
                distance[c] += i - last_seen.get(c, 0) - 1
            else:
                distance[c] = 0
            last_seen[c] = i

        print(f"counts = {count}")
        print(f"distances = {distance}")
        print(f"last_seen = {last_seen}")

        n = 0
        for c, freq in count.items():
            print(f"checking for character {c}")
            d = distance[c]
            if d == k:
                n = max(n, freq + k)
            elif d < k:
                tmp_n = freq + d
                k = k - d
                if len(s) - freq - d > k:
                    tmp_n += k
                else:
                    tmp_n += len(s) - freq - d
                n = max(n, tmp_n)
            else:
                tmp_n = freq + k
                r = k - d
                if len(s) - freq >= r:
                    tmp_n += r
                else:
                    tmp_n += len(s) - freq
                n = max(n, tmp_n)

        return n