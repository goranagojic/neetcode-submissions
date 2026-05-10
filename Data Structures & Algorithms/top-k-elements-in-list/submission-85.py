import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k frequent elements using heap

        # calculate frequences
        freqs = dict()
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        # prepare data for heap - number frequency pairs
        freq_l = list()
        for num, freq in freqs.items():
            freq_l.append((freq, num))

        # add to min heap - keep the heap of size k
        freq_h = list()
        heapq.heapify(freq_h)

        for freq, num in freq_l:
            heapq.heappush(freq_h, (freq, num))
            if len(freq_h) > k:
                heapq.heappop(freq_h)
            
        return [num for freq, num in freq_h]


        # when heap overgrows k and becomes k+1, pop the min element
        