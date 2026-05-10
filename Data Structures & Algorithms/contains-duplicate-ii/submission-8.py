class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # iterate over the array in window size k, add elemnets to the set to detect duplicates
        # control set size to keep window of size k
        # time complexity O(N) - iterating through the array once (avg. O(1) to add elem. to the set, O(1) to remove)
        # space complexity O(k) - for hashset size

        if k == 0: # no duplicates since there is no window
            return False

        window = set([nums[0]])
        for i in range(1, len(nums)):
            # iterate over the array using window k
            # window size is built-in through control of hashset size
            # hashset is used to easily detect duplicates
            if nums[i] in window:
                return True # found duplicate
            
            window.add(nums[i])
            if len(window) > k: # but window size can grow behind k when continuously adding elements 
                window.remove(nums[i-k]) # so when you add k+1 element, remove the 1st element from the window (that one is on the index nums[i-k])
            
        return False
