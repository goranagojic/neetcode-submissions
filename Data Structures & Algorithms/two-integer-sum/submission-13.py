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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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