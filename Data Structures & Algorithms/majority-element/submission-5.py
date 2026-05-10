from collections import defaultdict

class Solution:

    def majorityElementHashMap(self, nums: List[int]) -> int:
        # total algorithm time complexity O(N)
        
        # count num of occurences for each unique value in the array
        # time complexity: O(N)
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        # find the value that is majority
        # since it is guaranteed that there is majority, when you find the first you may exit because there is no other value fullfiling majority condition
        # time complexity O(G) - bounded by O(N) since there will always be less then N groups to iterate through (~N/2)
        threashold = len(nums) / 2
        for num, cnt in counts.items():
            if cnt > threashold:
                return num
            
        return nums[0] # this should never execute

    def majorityElementSorting(self, nums: List[int]) -> int:
        # time complexity O(nlogn)

        nums.sort() # O(nlogn)
        return nums[len(nums) // 2] #O(1)

    def majorityElement(self, nums: List[int]) -> int:
        # Bayer-Moore voting algorithm for finding a majority element
        # complexity:
            # time: O(N)
            # space: O(1)

        candidate, cnt = 0, 0

        for num in nums:
            if cnt == 0:
                candidate = num
                
            if num == candidate:
                cnt += 1
            else:
                cnt -= 1

        return candidate
        

    # TODO implement solution using randomization
    # todo Boyer-Moore Voting Algorithm?