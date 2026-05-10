# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         complements = dict()

#         for i, num in enumerate(nums):
#             complement = target - num
#             if complements.get(complement) != None:
#                 c_idx = complements[complement]
#                 ret_val = [i, c_idx] if i < c_idx else [c_idx, i]
#                 return ret_val
#             complements[num] = i     


class Solution:
    def twoSumTmp(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the idea: iterate through the array and in paralel keep a hashmap with values complement to the elements that has been seen
        # in this way, when you get to the next element, you may check if that element is a complement of some previously seen element
        # since the task requires indices to be returned, the value in hashmap will be the index of the element for which the complement is added to the hashmap
        # hashmap key will, naturally, be the complement itself for fast compelement lookup
        # when you return indices, you always know the index of the current element and you will get the index of the secod element from the hashmap
        # complexity
        #   time: O(n) - iterating throught the whole array, access hashmap elem. O(1), add to hashmap O(1) amortized
        #   space: O(n) - for hashmap, may have at most n elements

        
        complements = dict() # (complement value, index in array pairs) # bounded by O(n)

        for i in range(len(nums)): # O(n) time
            num = nums[i]            # O(1) time, O(1) space

            i_am_complement = num in complements # same
            if i_am_complement: 
                idx = complements[num]
                if i < idx:
                    return [i, idx]
                else:
                    return [idx, i]
            else:
                complements[target - num] = i