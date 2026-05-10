class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Algorithm is based on character count in strings s and t.
        # When different character count is found, False is returned.
        # Edge case: when s and t are of different lenght, they are not anagrams.

        # Check length
        if len(s) != len(t):
            return False
        
        # Check character count
        unique_characters_s = set(s)
        for c in unique_characters_s:
            if s.count(c) != t.count(c):
                # Not anagram -> character count differs
                return False

        return True
        