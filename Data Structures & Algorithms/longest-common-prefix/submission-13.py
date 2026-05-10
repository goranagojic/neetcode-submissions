class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        prefix = strs[0]
        for s in strs[1:]:
            tmp_prefix = ""
            for p_idx in range(len(prefix)):
                if p_idx == len(s):
                    break
                if prefix[p_idx] != s[p_idx]:
                    break
                else:
                    tmp_prefix += prefix[p_idx]
            prefix = tmp_prefix

        return prefix
            