class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res


    # def majorityElement(self, nums: List[int]) -> List[int]:
    #     # the most efficient solution for this problem is to use buyer-moore voting algorithm
    #     # there is no guarantee that there will be a majority element appearing n/3 times

    #     # find candidates using buyer-moore voting algorithm
    #     candidate1, candidate2 = -1, -1
    #     cnt1, cnt2 = 0, 0
    #     for num in nums:
    #         if cnt1 == 0 and num != candidate2:
    #             candidate1 = num
    #         if cnt2 == 0 and num != candidate1:
    #             candidate2 = num
            
    #         if candidate1 == num:
    #             cnt1 += 1
    #         elif candidate2 == num:
    #             cnt2 += 1
    #         else:
    #             if cnt1 < cnt2 and cnt1 > 0:
    #                 cnt1 -= 1
    #             elif cnt2 < cnt1 and cnt2 > 0:
    #                 cnt2 -= 1
    #             else:
    #                 cnt1 -= 1


    #     # check for candidates if there is more then n // 3 appearances of each
    #     n_candidate1, n_candidate2 = 0, 0
    #     for num in nums:
    #         if num == candidate1:
    #             n_candidate1 += 1
    #         elif num == candidate2:
    #             n_candidate2 += 1
    #     print(f"candidate 1 = {candidate1} {n_candidate1}")
    #     print(f"candidate 2 = {candidate2} {n_candidate2}")

    #     # append each candidate that satisfies the condition
    #     result = []
    #     if n_candidate1 > len(nums) // 3:
    #         result.append(candidate1)
    #     if n_candidate2 > len(nums) // 3:
    #         result.append(candidate2)

    #     return result

