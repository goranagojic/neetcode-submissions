class Solution:
    def productExceptSelfInefficient(self, nums: List[int]) -> List[int]:
        # time complexity of the solution - between O(n) (when no num is zero) and O(n^2) (when all elements in num are zeros)
        # space complexity O(n) since the output is a list of size n

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
                # when current element iz 0, that means that the product is zero and cannot be used in that
                # form for multiplication calculation
                # so, for zeros calculate the product by iterating through all array elements except this one
                p = 1
                # O(n)
                for j, n in enumerate(nums):
                    if i != j:
                        p *= n
                output[i] = p

        return output


    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # this solution is O(n)

        zeros = nums.count(0)

        # zero > 1 all products will be zero
        product, non_zero_product = 1, 1
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            for num in nums:
                product *= num
                if num == 0:
                    continue
                non_zero_product *= num
        else:
            for num in nums:
                product *= num

        output = [0] * len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                output[i] = non_zero_product
            else:
                output[i] = product // num

        return output

    def productExceptSelfWithDivision(self, nums: List[int]) -> List[int]:
        # this solution is O(n)

        zeros = nums.count(0)

        # zero > 1 all products will be zero
        product = 1
        output = [0] * len(nums)
        if zeros > 1:
            # case 1: multiple zeros in nums, all partial products will be 0
            return [0] * len(nums)
        elif zeros == 1:
            # case 2: a single zero in nums, partial products for all elements except this one will be 0
            # for zero element it will be the product of all other elements in num
            for num in nums:
                if num == 0:
                    continue
                product *= num

            for i, num in enumerate(nums):
                if num != 0:
                    continue
                output[i] = product
        else:
            # the last case: no zero elements in the array
            # partial sum of each element is calculated like product // that element
            for num in nums:
                product *= num
        
            for i, num in enumerate(nums):
                output[i] = product // num

        return output

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)

        # zero > 1 all products will be zero
        product = 1
        output = [0] * len(nums)
        if zeros > 1:
            # case 1: multiple zeros in nums, all partial products will be 0
            return [0] * len(nums)
        elif zeros == 1:
            # case 2: a single zero in nums, partial products for all elements except this one will be 0
            # for zero element it will be the product of all other elements in num
            for num in nums:
                if num == 0:
                    continue
                product *= num

            for i, num in enumerate(nums):
                if num != 0:
                    continue
                output[i] = product
        else:
            # the last case: no zero elements in the array
            # partial sum of each element is calculated like product // that element
            products_before, products_after = [1] * len(nums), [1] * len(nums)

            # products before
            n = len(nums)
            for i in range(1, n, 1):
                products_before[i] = products_before[i-1] * nums[i-1]
            print(products_before)

            for i in range(n-2, -1, -1):
                products_after[i] = products_after[i+1] * nums[i+1]
            print(products_after)

            for i, num in enumerate(nums):
                output[i] = products_before[i] * products_after[i]

        return output
