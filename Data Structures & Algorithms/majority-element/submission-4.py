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

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
        