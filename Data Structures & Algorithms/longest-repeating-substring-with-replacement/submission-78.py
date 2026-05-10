class Solution:
    def characterReplacementBruteForce(self, s: str, k: int) -> int:
        # input: s - uppercase eng. only
        # input: k - max num. of chars to be replaced with any other char

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

    def characterReplacement(self, s: str, k: int) -> int:
        # input: s - uppercase eng. only
        # input: k - max num. of chars to be replaced with any other char

        # brute force
        # check every substring
        l, r = 0, 0
        res = 0
        
        # two pointer in a while alternative
        window = {chr(ch): 0 for ch in range(ord('A'), ord('Z') + 1)}
        max_cnt, max_ch = 0, ''
        window_size = 0 
        while r < len(s):
            # add new char to the window
            window[s[r]] += 1
            window_size += 1

            # update max_char / cnt
            if window[s[r]] > max_cnt:
                max_cnt = window[s[r]]
                max_ch = s[r]

            # update max substring len
            if window_size - max_cnt <= k:
                res = max(res, window_size) # this will also get an empty string


            while l <= r and window_size - max_cnt > k: # l <= r is redundant condition which will never evaluate to false

                # update window / size
                window[s[l]] -= 1
                window_size -= 1

                # update max_char / cnt
                # when max_ch is excluded from the window, new max_ch/max_cnt has to be calculated because 
                if max_ch == s[l]:
                    max_ch = max(window, key=window.get)
                    max_cnt = window[max_ch]
                l += 1
            # grow window further
            r += 1


        return res