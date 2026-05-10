class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input: s - uppercase eng. only
        # input: k - max num. of chars to be replaced with any other char

        # brute force
        # check every substring
        l, r = 0, 0
        res = 0
        
        # two pointer in a while alternative
        while l < len(s):
            window = {chr(ch): 0 for ch in range(ord('A'), ord('Z') + 1)}
            max_cnt, max_ch = 0, ''
            window_size = 0        
            # when total - max_cnt (remaining chars in window) <= k, means they can be substituted and longest substring with
            # k replacements formed
            r = l
            while r < len(s):
                ch = s[r]
                window_size += 1
                window[ch] += 1
                if max_cnt < window[ch]:
                    max_cnt = window[ch]
                    max_ch = ch
                print(f'l = {l}, r = {r}, max-cnt: {max_cnt}, total: {window_size}')
                if window_size - max_cnt <= k:
                    res = max(res, window_size)
                else:
                    break
                r += 1
            l += 1
            print(window)

        # brute force solution - checks every substring starting on different s char - substring is called window
        # for each window, we track total number of chars in window and count of the most frequent char in the window
        # when total num - most freq cnt is leq to k, means all other chars can be replaced with most freq. char to get
        # a valid substring (according to assignment demands, just one character in the string)
        # if there are more then k chars to replace in window, the algorithm breaks early for that window start on s[l] char
        # The solution has O(n2) time complexity
        # in more detail:
        #     - O(n) (outer loop) * (O(26) to create window dict + O(n) to iterate again through s) -> O(26n) + O(n2) 
        #        -> approximated with O(n2)
        # Space complexity:
        #     - O(1) - constant memory (i.e. O(26) for dict)
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
                    break                       # more then k chars to replace in window, no need to interate further

        return res