import heapq

class Solution:
    def topKFrequentGlogG(self, nums: List[int], k: int) -> List[int]:
        # so the dominant element in time complexity of this algorithms is O(glogg) bounded by O(nlogn)
        # space complexity bounded by O(n)

        # get each element frequency as value
        # time complexity: O(n) 
        # space complexity: O(g+1) - number of groups + 1 count var for each group, again bounded by n, so O(n)
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # now get values to be "keys"
        # since there can be duplicates we use list
        # time complexity: O(g) bounded by O(n)
        # space complexity: O(g) bounded by O(n)
        freqs_l = list()
        for num, freq in freqs.items():
            freqs_l.append((freq, num))

        # now sort by frequency desc 
        # time complexity: default sorting O(glogg)
        # space complexity O(g) bounded by O(n)
        freqs_l = sorted(freqs_l, key=lambda f: f[0], reverse=True)
        # print(freqs_l)

        # ... and return top k elements
        # O(k)
        return [num for _, num in freqs_l[:k]]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count frequences
        frequences = dict()
        for num in nums:
            frequences[num] = 1 + frequences.get(num, 0)

        # prepare data for max heap
        freq_l = list()
        for num, freq in frequences.items():
            freq_l.append((-freq, num))

        # create max heap using min heap
        heapq.heapify(freq_l)
        print(freq_l)

        top_k = list()
        while k:
            top_k.append(heapq.heappop(freq_l)[1])
            k -= 1

        return top_k




        


         
        