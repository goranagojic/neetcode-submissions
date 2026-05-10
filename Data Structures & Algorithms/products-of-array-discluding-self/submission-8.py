class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time complexity of the solution - between O(n) (when no num is zero) and O(n^2) (when all elements in num are zeros)

        product = 1
        # O(n)
        for num in nums:
            product *= num

        output = [0] * len(nums)
        # O(n)
        for i, num in enumerate(nums):
            if num != 0:
                output[i] = product // num
            else:
                p = 1
                # O(n)
                for j, n in enumerate(nums):
                    if i != j:
                        p *= n
                output[i] = p

        return output