class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # SOLUTION 1 - Calculate a frequency dictionary for all values in num list
        # time complexity: O(n)
        frequencies = dict()    # key: number, value: frequency
        for num in nums:
            if frequencies.get(num) is None:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        # then get the list of pairs
        freq_list = list(frequencies.items())
        # sort by frequency
        freq_list.sort(key=lambda v: v[1], reverse=True)

        return [num for num, freq in freq_list[:k]]

        # SOLUTION 2 - Use heap data structure - this structure is often used in TopK problems
        # TODO