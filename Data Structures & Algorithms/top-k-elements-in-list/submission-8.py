class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = dict()
        for num in nums:
            if frequencies.get(num) is None:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        freq_list = list(frequencies.items())
        freq_list.sort(key=lambda v: v[1], reverse=True)

        return [num for num, freq in freq_list[:k]]