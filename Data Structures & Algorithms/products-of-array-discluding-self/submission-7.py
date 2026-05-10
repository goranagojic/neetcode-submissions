class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        for num in nums:
            product *= num

        output = [0] * len(nums)
        for i, num in enumerate(nums):
            if num != 0:
                output[i] = product // num
            else:
                p = 1
                for j, n in enumerate(nums):
                    if i != j:
                        p *= n
                output[i] = p

        return output