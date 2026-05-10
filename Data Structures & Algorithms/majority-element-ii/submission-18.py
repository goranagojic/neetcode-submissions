class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = -1, -1
        cnt1, cnt2 = 0, 0

        for num in nums:
            if cnt1 == 0 and num != candidate2:
                candidate1 = num
            if cnt2 == 0 and num != candidate1:
                candidate2 = num

            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            else:
                continue
        print(f"candidate 1 = {candidate1} {cnt1}")
        print(f"candidate 2 = {candidate2} {cnt2}")

        majorities = []
        if cnt1 > len(nums) // 3:
            majorities.append(candidate1)
        if cnt2 > len(nums) // 3:
            majorities.append(candidate2)

        return majorities