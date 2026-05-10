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
        
        def _find_common_prefix(s1: str, s2: str) -> str:
            
            prefix = s1

            idx = -1
            for i in range(min(len(prefix), len(s2))):
                if prefix[i] == s2[i]:
                    idx = i
                else:
                    break

            return prefix[:idx+1]
                


        # strs.sort() # ERROR this actually wasn't needed - so the error is to assume it is needed
        # 1) INITIAL SOLUTION
        if not strs:
            return ""

        # prefix = strs[0]
        # # iterate over strings to compare them to the existing prefix
        # for s in strs[1:]:
        #     # ind max overlap between prefix and current str
        #     p_idx = 0
        #     for p_idx in range(len(prefix)):
        #         if p_idx == len(s):             # string ended, prefix completed
        #             break
        #         if prefix[p_idx] != s[p_idx]:   # first unmached character, prefix completed
        #             break
        #         else:
        #             p_idx += 1
        #             # tmp_prefix += prefix[p_idx] # append character to prefix    # WARNING: appending char-by-char is quadric complexity of prefix length -> track index, then slice once!
        #     prefix = prefix[:p_idx]


        # 2b) simplified using the function
        prefix = strs[0]
        for s in strs[1:]:
            prefix = _find_common_prefix(prefix, s)

        # 2b) whole solution in one place using zip
        # for s in strs[1:]:
        #     tmp_idx = -1

        #     if s == "":
        #         return ""

        #     for i, (sc, pc) in enumerate(zip(s, prefix)): # zip makes character tuples 

        #         if sc == pc:
        #             tmp_idx = i
        #         else:
        #             prefix = "" if tmp_idx == -1 else prefix[:tmp_idx+1]
        #             break
        #     else:
        #         prefix = prefix[:tmp_idx+1]

        # 3) use sorting and intersection of the first and the last string
        # strs.sort()
        # prefix = _find_common_prefix(strs[0], strs[-1])

        return prefix
            