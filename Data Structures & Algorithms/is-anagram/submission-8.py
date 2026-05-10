class Solution:
    def isAnagramHashsets(self, s: str, t: str) -> bool:
        # Algorithm is based on character count in strings s and t.
        # When different character count is found, False is returned.
        # Edge cases: 
        #   1. When s and t are of different lenght, they are not anagrams.
        #   2. When s and t contain different characters, they are not anagrams.
        # asymptotic time complexity: O(N^2)
        # space complexity O(N)
        # ! this implementation has higher time+space complexity then recommended one

        # Check length
        if len(s) != len(t): # O(1)
            return False

        # Check characters
        unique_s, unique_t = set(s), set(t) # O(n) + O(m)
        if unique_s != unique_t:
            return False
        
        # Check character count
        unique_characters_s = set(s) # O(N)
        for c in unique_characters_s: # O(N') < O(N)
            if s.count(c) != t.count(c): # count -> O(N) + O(M) -> O(N+M)
                # Not anagram -> character count differs
                return False
                # final loop complexity: O(N')O(N+M) = O(N^2+M) which is O(N^2) in the worst case

        return True
        
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_char_cnt = [0] * (ord('z') - ord('a') + 1)
        for c in s:
            s_char_cnt[ord(c) - ord('a')] += 1

        t_char_cnt = [0] * (ord('z') - ord('a') + 1)
        for c in t:
            t_char_cnt[ord(c) - ord('a')] += 1

        if tuple(s_char_cnt) == tuple(t_char_cnt):
            return True
        
        return False