class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Task: ou are given an array of strings strs. Return the longest common prefix of all the strings. If there is no longest common prefix, return an empty string "".
        # Basic idea: assume the first string is a prefix for all other strings, 
        # and reduce the prefix when you find mismatch between the beginning of 
        # any string you compare to and the prefix. For this to work, the starting
        # array of string must be sorted.
        # Time complexity
        #   O(N) - iterate through array elements
        #       for each element, iterate through prefix:str pairs with avg. length M
        #       if M << N, time complexity is O(N)
        #       if M ~ N, time complexity is O(M)*O(N)
        #       if M >> N, time complexity is O(M)
        
        # strs.sort() # ERROR this actually wasn't needed
        if not strs:
            return ""

        prefix = strs[0]
        # iterate over strings to compare them to the existing prefix
        for s in strs[1:]:
            # ind max overlap between prefix and current str
            tmp_prefix = ""
            for p_idx in range(len(prefix)):
                if p_idx == len(s):             # string ended, prefix completed
                    break
                if prefix[p_idx] != s[p_idx]:   # first unmached character, prefix completed
                    break
                else:
                    tmp_prefix += prefix[p_idx] # append character to prefix    # WARNING: appending char-by-char is quadric complexity of prefix length -> track index, then slice once!
            prefix = tmp_prefix

        return prefix
            