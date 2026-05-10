class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input: s - uppercase eng. only
        # input: k - max num. of chars to be replaced with any other char

        # brute force
        # check every substring
        l, r = 0, 0
        res = 0
        
        # while l < len(s):
        #     window = {chr(ch): 0 for ch in range(ord('A'), ord('Z') + 1)}
        #     max_cnt, max_ch = 0, ''
        #     total = 0        
        #     # when total - max_cnt (remaining chars in window) <= k, means they can be substituted and longest substring with
        #     # k replacements formed
        #     r = l
        #     while r < len(s):
        #         ch = s[r]
        #         print(ch)
        #         total += 1
        #         window[ch] += 1
        #         if max_cnt < window[ch]:
        #             max_cnt = window[ch]
        #             max_ch = ch
        #         print(f'l = {l}, r = {r}, max-cnt: {max_cnt}, total: {total}')
        #         if total - max_cnt <= k:
        #             res = max(res, total)
        #         else:
        #             break
        #         r += 1
        #     l += 1
        #     print(window)

        for l in range(0, len(s)):
            window = {chr(ch): 0 for ch in range(ord('A'), ord('Z') + 1)}
            max_cnt, max_ch, window_size = 0, '', 0
            for r in range(l, len(s)):
                window_size += 1
                window[s[r]] += 1
                if max_cnt < window[s[r]]:
                    max_cnt = window[s[r]]
                    max_ch = s[r]
                if window_size - max_cnt <= k: # leq. chars to replace with k, valid substring
                    res = max(res, window_size)
                else:
                    break               # more then k chars to replace in window, no need to interate further

        return res