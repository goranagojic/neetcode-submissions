class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input: s - uppercase eng. only
        # input: k - max num. of chars to be replaced with any other char

        # brute force
        # check every substring
        l, r = 0, 0
        res = 0
        
        while l < len(s):
            window = {chr(ch): 0 for ch in range(ord('A'), ord('Z') + 1)}
            max_cnt, max_ch, total = 1, s[l], 1 # track how many chars has current window and cnt of the most repeating char
            window[s[l]] += 1
            # when total - max_cnt (remaining chars in window) <= k, means they can be substituted and longest substring with
            # k replacements formed
            r = l + 1
            while r < len(s):
                ch = s[r]
                print(ch)
                total += 1
                window[ch] += 1
                if max_cnt < window[ch]:
                    max_cnt = window[ch]
                    max_ch = ch
                print(f'l = {l}, r = {r}, max-cnt: {max_cnt}, total: {total}')
                if total - max_cnt <= k:
                    res = max(res, total)
                else:
                    break
                r += 1
            l += 1
            print(window)

        return res