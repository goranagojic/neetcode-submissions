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

        # TODO tasks
        # - understand why you don't need to sort in this implementation
        # - rewrite to avoid character appending
        # - reimplement that idea that when sorted i can use intersection between the first and the last element
        
        # strs.sort() # ERROR this actually wasn't needed - so the error is to assume it is needed
        # 1) INITIAL SOLUTION
        if not strs:
            return ""

        prefix = strs[0]
        # iterate over strings to compare them to the existing prefix
        for s in strs[1:]:
            # ind max overlap between prefix and current str
            p_idx = 0
            for p_idx in range(len(prefix)):
                if p_idx == len(s):             # string ended, prefix completed
                    break
                if prefix[p_idx] != s[p_idx]:   # first unmached character, prefix completed
                    break
                else:
                    p_idx += 1
                    # tmp_prefix += prefix[p_idx] # append character to prefix    # WARNING: appending char-by-char is quadric complexity of prefix length -> track index, then slice once!
            prefix = prefix[:p_idx]


        # 2) THE FIRST REFINEMENT
        # prefix = strs[0]
        # for s in strs[1:]:
        #     tmp_idx = -1

        #     if s == "":
        #         return ""

        #     for i, (sc, pc) in enumerate(zip(s, prefix)):

        #         if i == min(len(s), len(prefix)):
        #             prefix = prefix[:tmp_idx+1]
        #             break

        #         if sc == pc:
        #             tmp_idx = i
        #         else:
        #             prefix = "" if tmp_idx == -1 else prefix[:tmp_idx+1]
        #             break

        return prefix
            