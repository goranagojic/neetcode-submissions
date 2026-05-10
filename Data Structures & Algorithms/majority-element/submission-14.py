import random

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

    def majorityElementBayerMooreVoting(self, nums: List[int]) -> int:
        # Bayer-Moore voting algorithm for finding a majority element
        # complexity:
            # time: O(N)
            # space: O(1)
        # the algorithms says:
        # init candidate and cnt to - no candidate and 0
        # iterate over the array
        # if cnt == 0, assign new candidate
        # if candidate == current element, increase cnt, otherwise decrease cnt
        # rinse and repeat
        # at the end you end up with the majority element 
            # no check required if it is guarranteed that there is majority element in the array
            # otherwise you need to check if the element is majority
        # THIS IMPLEMENTATION IS SPECIFIC FOR MAJORITY ELEMENT BEING N/2
        # for N/3 there may be 2 kandidates, to i track two candidates/counts
        # for N/K there may be K-1 candidates, so i track K-1 candidates/counts

        candidate, cnt = 0, 0

        for num in nums:
            if cnt == 0:
                candidate = num
                
            if num == candidate:
                cnt += 1
            else:
                cnt -= 1

        if nums.count(candidate) > len(nums) / 2:
            return candidate

        return -1 # no candidate - this case will be never reached in this setup


    def majorityElement(self, nums: List[int]) -> int:

        iteration = 0
        while True:
            random_idx = random.randint(0, len(nums)-1)
            majority_val = nums[random_idx]

            if nums.count(majority_val) > len(nums) / 2:
                return majority_val

            iteration += 1
            print(iteration)


        

    # TODO implement solution using randomization
    # todo Boyer-Moore Voting Algorithm?